from reagentpy.clients import ReagentClient, ReagentResponse

class RepoClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def email_domains(self, repo: str | None = None, limit: int = 10, 
                      timezone: float | None = None, start_date: str | None = None, end_date: str | None = None):
        """Given a repository, get all the other organizations that contributing users are working in."""

        query_params = {
            "repo_name": repo,
            "limit": limit,
            "tz": timezone,
            "start_date": start_date,
            "end_date": end_date,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/repo/email_domains", params=query_params))

    def timezones(self, repo: str | None = None, email: str | None = None,
                      timezone: float | None = None, name: str | None = None):
        """Given a repo name, get number of commits and timezone data."""

        query_params = {
            "repo": repo,
            "email": email,
            "name": name,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/repo/timezones", params=query_params))
    

    def user_commit_data(self, repo: str | None = None, limit: int = 10, email: str | None = None, name: str | None = None,
                      timezone: float | None = None, start_date: str | None = None, end_date: str | None = None,
                      order_by_date: bool | None = None, include_other_repos: bool | None = None, format_in_rows: bool | None = None):
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