import os
import requests

from dotenv import load_dotenv

import pandas as pd

from reagentpy.constants import VERSION, REAGENTPY_USER_AGENT, REAGENT_BASE_URL

class ReagentResponse:

    response: requests.Response = None

    status_code: int = None

    metadata: bool = False

    def __init__(self, response: requests.Response, metadata: bool = False):
        self.response = response
        self.status_code = response.status_code

    def dict(self):
        if self.metadata:
            return self.response.json()
        else:
            if 'results' in self.response.json():
                return self.response.json().get('results')
            else:
                return self.response.json()
    
    def df(self):
        return pd.json_normalize(self.dict())

    def json(self):
        return self.df().to_json(orient="records")
    
    def csv(self):
        return self.df().to_csv(index=False)
    
    def text(self):
        return self.csv()
    

class ReagentClient:

    version: str = None

    reagent_base_url: str = None

    reagent_api_key: str = None

    session: requests.Session = None

    def __init__(self, reagent_api_key: str = None):

        # Set the version
        self.version = "0.1.0"

        # Set the user agent
        self.user_agent = f"{REAGENTPY_USER_AGENT}/{self.version}"

        # Set the base URL
        self.reagent_base_url = REAGENT_BASE_URL

        if reagent_api_key:
            self.reagent_api_key = reagent_api_key
        else:
            # Load environment variables from a .env file
            load_dotenv()
            self.reagent_api_key = os.getenv("REAGENT_API_KEY")

        # Initialize a new requests session
        self.init_session()

    def init_session(self):
        """Initialize a new requests session."""
        
        # Create a requests session
        self.session = requests.Session()

        # Set the authorization header
        if not self.reagent_api_key:
            raise ValueError("Reagent API key environment variable not set or missing. Try \"reagent login\" to set the API key.")
        self.session.headers.update({
            "Authorization": f"Basic {self.reagent_api_key}"
        })

        # Set user agent
        self.session.headers.update(
            {
                "User-Agent": f"{self.user_agent}"
            }
        )
