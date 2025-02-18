from typing import Optional
from reagentpy.clients import ReagentResponse
from reagentpy.ReagentClient import ReagentClient

class EnrichmentsClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def hibp(self, repo: Optional[str] = None, limit: int = 10, breach: Optional[str] = None,
                email: Optional[str] = None, timezone: Optional[str] = None):
        """Given a repo name or email address, get all data breaches the entity is a part of."""

        query_params = {
            "repo": repo,
            "limit": limit,
            "breach": breach,
            "email": email,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/hibp", params=query_params))

    def similar_repos(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None, 
                        timezone: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
        """Given a repository, get similar organizations and tags common between them."""

        query_params = {
            "repo": repo,
            "email": email,
            "timezone": timezone,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/similar_repos", params=query_params))
    
    def timezone_spoof(self, repo: Optional[str] = None, limit: int = 10):
        """Given a repo name, get all fabricated timezone information."""

        query_params = {
            "repo": repo,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/timezone_spoof", params=query_params))
    
    def topics(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None,
                        timezone: Optional[str] = None, name: Optional[str] = None):
        """Get topics (categories of code based on commit messages and repository READMEs) by repository or user."""

        query_params = {
            "repo": repo,
            "limit": limit,
            "email": email,
            "name": name,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/topics", params=query_params))
    
    def threat_summary(self, repo: Optional[str] = None, adversarial: Optional[bool] = None, limit: int = 10):
        """Given a kind of threat and repo name, get threat score info (project fragmentation, unfocused contribution, context switching, interactive churn)."""
        query_params = {
            "repo": repo,
            "adversarial": adversarial,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/threat/summary", params=query_params))
    
    def threat_score(self, repo: Optional[str] = None):
        """Given a kind of threat and repo name, get threat score info (project fragmentation, unfocused contribution, context switching, interactive churn)."""
        query_params = {
            "repo": repo
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/threat/score", params=query_params))
    
    def threat_scores_for_visualizations(self, repo: Optional[str] = None, limit: Optional[int] = None):
        """Given a repo name, get threat scores for visualization purposes."""
        query_params = {
            "repo": repo,
            "limit": limit
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/visualizations/get_threat_scores", params=query_params))
    
    def hibp_for_visualizations(self, repo: Optional[str] = None, limit: int = 50):
        """Given a repo name, get hibp data for visualization purposes."""
        query_params = {
            "repo": repo,
            "limit": limit
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/visualizations/hibp", params=query_params))
