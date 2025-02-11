from typing import Optional
from reagentpy.clients import ReagentResponse
from reagentpy.ReagentClient import ReagentClient

class CommunityClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def maintainers(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None,
                      name: Optional[str] = None, timezone: Optional[float] = None, file: Optional[str] = None, 
                      hibp: Optional[bool] = None, community: Optional[str] = None):
        """Given a repo or user information, get all the maintainers of mutual file communities."""

        query_params = {
            "repo": repo,
            "timezone": timezone,
            "email": email,
            "name": name,
            "limit": limit,
            "file": file,
            "hibp": hibp,
            "community": community,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/community/maintainers", params=query_params))

    def communities(self, repo: Optional[str] = None, limit: int = 10, timezone: Optional[float] = None,
                      start_date: Optional[str] = None, end_date: Optional[str] = None):
        """Get all file communities (usually features) in a repo, given repo information."""

        query_params = {
            "repo": repo,
            "timezone": timezone,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/community/communities", params=query_params))