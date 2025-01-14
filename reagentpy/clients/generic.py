from reagentpy.clients import ReagentResponse
from reagentpy.ReagentClient import ReagentClient

class GenericClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def get(self, endpoint: str, **kwargs):
        """Generic get request to the Reagent API."""
        return ReagentResponse(self.session.get(f"{self.reagent_base_url}{endpoint}", params=kwargs))
    
    def post(self, endpoint: str, **kwargs):
        """Generic post request to the Reagent API."""
        return ReagentResponse(self.session.post(f"{self.reagent_base_url}{endpoint}", json=kwargs))