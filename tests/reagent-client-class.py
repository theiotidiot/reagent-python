# FILE: test_reagent.py
import os
import pytest
from reagentpy.ReagentClient import ReagentClient
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv

load_dotenv()
REAGENT_API_KEY = os.environ.get('REAGENT_API_KEY')

@patch.dict('os.environ', {'REAGENT_API_KEY': REAGENT_API_KEY})
@patch('requests.Session')
def test_reagent(mock_session):
    # Mock the session object
    mock_session_instance = MagicMock()
    mock_session.return_value = mock_session_instance

    # Initialize the Reagent class
    client = ReagentClient()

    # Initialize the ReagentClient class

    # Check if the API key is set correctly
    assert client.reagent_api_key == REAGENT_API_KEY

    # Check if the session is created
    mock_session.assert_called_once()

    # Check if the authorization header is set correctly
    mock_session_instance.headers.update.assert_any_call({
        'Authorization': f'Basic {REAGENT_API_KEY}'
    })

    # Check if the user agent header is set correctly
    mock_session_instance.headers.update.assert_any_call({
        'User-Agent': 'reagentpy/0.1.0'
    })

    # Mock a response for the _request method
    mock_response = MagicMock()
    mock_response.json.return_value = {'status': 'ok'}
    mock_session_instance.request.return_value = mock_response

    # Test the _request method
    response = client.session.request("GET", f"{client.reagent_base_url}/status", params=None)
    assert response.json() == {'status': 'ok'}
    mock_session_instance.request.assert_called_once_with('GET', 'https://api.reagentanalytics.com/v1/status', params=None)


if __name__ == "__main__":
    pytest.main()
