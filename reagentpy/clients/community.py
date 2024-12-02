from reagentpy.clients import ReagentClient, ReagentResponse

class CommunityClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def maintainers(self, repo: str | None = None, limit: int = 10, email: str | None = None,
                      name: str | None = None, timezone: float | None = None, file: str | None = None, 
                      hibp: bool | None = None, community: str | None = None):
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

    def communities(self, repo: str | None = None, limit: int = 10, timezone: float | None = None,
                      start_date: str | None = None, end_date: str | None = None):
        """Get all file communities (usually features) in a repo, given repo information."""

        query_params = {
            "repo": repo,
            "timezone": timezone,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/community/communities", params=query_params))