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
