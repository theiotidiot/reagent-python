from reagentpy.clients import ReagentResponse
from reagentpy.ReagentClient import ReagentClient

class CommitClient(ReagentClient):
    def __init__(self):
        super().__init__()
        
    def data(self, repo: str | None = None, limit: int = 50, email: str | None = None,
            timezone: float | None = None, start_date: str | None = None, end_date: str | None = None, debug: bool = False):
        """Given an email or repo name, get time info on all the commits a user or set of users has committed."""

        query_params = {
            "repo": repo,
            "limit": limit,
            "email": email,
            "timezone": timezone,
            "start_date": start_date,
            "end_date": end_date,
            "debug": debug
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/commit/data", params=query_params))