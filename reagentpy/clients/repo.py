from reagentpy.clients import ReagentClient, ReagentResponse
from typing import Optional

class RepoClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def email_domains(self, repo: Optional[str] = None, limit: int = 10, 
                      timezone: Optional[float] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
        """Given a repository, get all the other organizations that contributing users are working in."""

        query_params = {
            "repo_name": repo,
            "limit": limit,
            "tz": timezone,
            "start_date": start_date,
            "end_date": end_date,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/repo/email_domains", params=query_params))

    def timezones(self, repo: Optional[str] = None, email: Optional[str] = None,
                      timezone: Optional[float] = None, name: Optional[str] = None):
        """Given a repo name, get number of commits and timezone data."""

        query_params = {
            "repo": repo,
            "email": email,
            "name": name,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/repo/timezones", params=query_params))
    

    def user_commit_data(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None, name: Optional[str] = None,
                      timezone: Optional[float] = None, start_date: Optional[str] = None, end_date: Optional[str] = None,
                      order_by_date: Optional[bool] = None, include_other_repos: Optional[bool] = None, format_in_rows: Optional[bool] = None):
        """Given a repo name and timezone, get users above a certain threshold for finer-grained intelligence."""

        query_params = {
            "repo": repo,
            "limit": limit,
            "email": email,
            "name": name,
            "tz": timezone,
            "start_date": start_date,
            "end_date": end_date,
            "order_by_date": order_by_date,
            "include_other_repos": include_other_repos,
            "format_in_rows": format_in_rows,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/repo/user_commit_data", params=query_params))