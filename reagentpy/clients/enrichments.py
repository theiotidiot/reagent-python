from reagentpy.clients import ReagentClient, ReagentResponse

class EnrichmentsClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def foreign_influence(self, entity_name: str | None = None, limit: int = 10, entity_type: str | None = None,
                      no_unspecified: bool | None = None, start_date: str | None = None, end_date: str | None = None):
        """Given a repo name, get a snapshot of foreign influence on all commits in the repo."""

        query_params = {
            "entity_name": entity_name,
            "start_date": start_date,
            "end_date": end_date,
            "no_unspecified": no_unspecified,
            "entity_type": entity_type,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/foreign_influence", params=query_params))

    def hibp(self, repo: str | None = None, limit: int = 10, breach: str | None = None,
                email: str | None = None, timezone: str | None = None):
        """Given a repo name or email address, get all data breaches the entity is a part of."""

        query_params = {
            "repo": repo,
            "limit": limit,
            "breach": breach,
            "email": email,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/hibp", params=query_params))

    def similar_repos(self, repo: str | None = None, limit: int = 10, email: str | None = None, 
                        timezone: str | None = None, start_date: str | None = None, end_date: str | None = None):
        """Given a repository, get similar organizations and tags common between them."""

        query_params = {
            "repo_name": repo,
            "email": email,
            "timezone": timezone,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/similar_repos", params=query_params))
    
    def timezone_spoof(self, repo: str | None = None, limit: int = 10):
        """Given a repo name, get all fabricated timezone information."""

        query_params = {
            "repo_name": repo,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/timezone_spoof", params=query_params))
    
    def topics(self, repo: str | None = None, limit: int = 10, email: str | None = None,
                        timezone: str | None = None, name: str | None = None):
        """Get topics (categories of code based on commit messages and repository READMEs) by repository or user."""

        query_params = {
            "repo_name": repo,
            "limit": limit,
            "email": email,
            "name": name,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/topics", params=query_params))
    
    def threat_summary(self, repo: str | None = None, adversarial: bool | None = None, limit: int = 10):
        """Given a kind of threat and repo name, get threat score info (project fragmentation, unfocused contribution, context switching, interactive churn)."""
        query_params = {
            "repo_name": repo,
            "adversarial": adversarial,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/threat/summary", params=query_params))
    
    def threat_score(self, repo: str | None = None):
        """Given a kind of threat and repo name, get threat score info (project fragmentation, unfocused contribution, context switching, interactive churn)."""
        query_params = {
            "repo": repo
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/threat/score", params=query_params))
    
    def threat_scores_for_visualizations(self, repo: str | None = None, limit: int = 50):
        """Given a repo name, get threat scores for visualization purposes."""
        query_params = {
            "repo": repo,
            "limit": limit
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/visualizations/get_threat_scores", params=query_params))
    
    def hibp_for_visualizations(self, repo: str | None = None, limit: int = 50):
        """Given a repo name, get hibp data for visualization purposes."""
        query_params = {
            "repo": repo,
            "limit": limit
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/visualizations/get_hibp", params=query_params))
