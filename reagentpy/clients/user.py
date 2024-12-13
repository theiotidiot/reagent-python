from reagentpy.clients import ReagentClient, ReagentResponse
from typing import Optional

class UserClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def commit_file_community(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None, name: Optional[str] = None,
                      order_by_date: Optional[bool] = None, format_in_rows: Optional[bool] = None,
                      timezone: Optional[float] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
        """Get threat scores, repos, and top developers on files."""

        query_params = {
            "repo": repo,
            "email": email,
            "name": name,
            "limit": limit,
            "timezone": timezone,
            "order_by_date": order_by_date,
            "start_date": start_date,
            "end_date": end_date,
            "format_in_rows": format_in_rows,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/user/commit_file_community", params=query_params))

    def post_patch(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None,
                      timezone: Optional[float] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
        """Get everything a user has done, sorting by most recent suspicious activity and whether their potentially introduced security vulnerabilities have been patched."""

        query_params = {
            "repo": repo,
            "limit": limit,
            "email": email,
            "tz": timezone,
            "sdate": start_date,
            "edate": end_date,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/user/post_patch", params=query_params))


    def profile(self, limit: int = 10, email: Optional[str] = None, name: Optional[str] = None,
                      timezone: Optional[float] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
        """Get contributor profiles for a given user."""

        query_params = {
            "limit": limit,
            "email": email,
            "name": name,
            "tz": timezone,
            "sdate": start_date,
            "edate": end_date,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/user/profile", params=query_params))