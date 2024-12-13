from reagentpy.clients import ReagentClient, ReagentResponse
from typing import Optional

class EnrichmentsClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def foreign_influence(self, entity_name: Optional[str] = None, limit: int = 10, entity_type: Optional[str] = None,
                      no_unspecified: Optional[bool] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
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
            "repo_name": repo,
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
            "repo_name": repo,
            "limit": limit,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/timezone_spoof", params=query_params))
    
    def topics(self, repo: Optional[str] = None, limit: int = 10, email: Optional[str] = None,
                        timezone: Optional[str] = None, name: Optional[str] = None):
        """Get topics (categories of code based on commit messages and repository READMEs) by repository or user."""

        query_params = {
            "repo_name": repo,
            "limit": limit,
            "email": email,
            "name": name,
            "timezone": timezone,
        }

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/enrichments/topics", params=query_params))
    
    def threat_summary(self, repo: Optional[str] = None, adversarial: Optional[bool] = None, limit: int = 10):
        """Given a kind of threat and repo name, get threat score info (project fragmentation, unfocused contribution, context switching, interactive churn)."""
        query_params = {
            "repo_name": repo,
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
    
