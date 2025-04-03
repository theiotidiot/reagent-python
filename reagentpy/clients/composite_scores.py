from typing import Optional
from reagentpy.clients import ReagentResponse
from reagentpy.ReagentClient import ReagentClient

class CompositeClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def nonadversarial_components(self, repo: str):
        """
        Given NON-OPTIONAL:
            - repository name (formatted "parent/repo_name", case-sensitive)
        get threat score info (project fragmentation, unfocused contribution, context switching, interactive churn).
        
        Project Fragmentation is defined as the ratio of files within a repository edited by ten or more developers to files 
        within a repository edited by less than ten developers.  The significance factor for this function is r = 16, meaning that
        a file is sixteen times more likely to contain a vulnerability if ten or more developers have contributed to it.

        Unfocused Contribution is measured by taking the average pagerank of each file within a repo.  The significance factor for 
        this function is r = .4497, meaning that vulnerabilities scale proportionally with developer multitasking (per file) with a rate of about half.

        Context Switching is calculated by taking the average weekly density of distinct file communities users commit to each week.  
        The significance factor for this function is r = 0.17, meaning there is a small but significant correllation with vulnerabilities introduced to distinct file communities
        that each developer contributes to.  File communities are groups of files that are typically modified together, and roughly translate to "features" or "modules" in a codebase.

        Interactive Churn is the average weekly number of user interactions a file has, scaled by how recent each action is.  The 
        significance factor for this function is r = 0.16, meaning there is a small but significant correllation with vulnerability introduction
        to the number of lines of other peoples' code a developer edits.

        Returns project fragmentation score, unfocused contribution score, context switching score, and interactive churn score, all out of ten.
        """
        query_params = {"repo": repo}

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/metadata-risk/components", params=query_params))

    def nonadversarial_total(self, repo: str):
        """
        Given NON-OPTIONAL:
            - repository name (formatted "parent/repo_name", case-sensitive)
        get HIGH-LEVEL AVERAGE SUMMARY OF project fragmentation, unfocused contribution, context switching, interactive churn.

        This takes the average percentages of project fragmentation, unfocused contribution, context switching, and interactive churn, and returns
        it as an average percent of commits to be worried about.  
        
        Calculations change when a category is "maxed out" (has a percentage of 100%), since that indicates an extraordinary level of
        risk in that category. In that case, the average is divided by one less than the original number of categories so the top-level percentage
        of risk is higher.

        Returns HIGH-LEVEL AVERAGE SUMMARY OF project fragmentation, unfocused contribution, context switching, interactive churn.
        """
        query_params = {"repo": repo}

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/metadata-risk/total", params=query_params))

    def nonadversarial_timezones(self, repo: str):
        """
        Given NON-OPTIONAL:
            - repository name (formatted "parent/repo_name", case-sensitive)
        get a list of all timezones commits were authored or committed in within the repository, broken down by percentage.

        Returns the percentage of commits by timezone. 
            
        Sorted by UTC offset in ascending order.
        """
        query_params = {"repo": repo}

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/metadata-risk/timezones", params=query_params))
    
    def adversarial_components(self, repo: str):
        """
        Given NON-OPTIONAL:
            - repository name (formatted "parent/repo_name", case-sensitive)
        get adversarial threat score info.  Adversarial threat scoring is broken down by commit percentage.

        Returns timezone spoof percentage, potentially adversarial timezone percentage, and non-work purpose-built account percentage.
        """
        query_params = {"repo": repo}

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/foreign-adversarial/components", params=query_params))

    def adversarial_timezones(self, repo: str):
        """
        Given NON-OPTIONAL:
            - repository name (formatted "parent/repo_name", case-sensitive)
        get a list of all POTENTIALLY ADVERSARIAL timezones commits were authored or committed in within the repository, broken down by percentage.

        Returns the percentage of commits by timezone, and corresponding major city. 
            
        Sorted by percentage in descending order, then UTC offset.
        """
        query_params = {"repo": repo}

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/foreign-adversarial/timezones", params=query_params))

    def adversarial_total(self, repo: str):
        """
        Given NON-OPTIONAL:
            - repository name (formatted "parent/repo_name", case-sensitive)
        get a HIGH-LEVEL AVERAGE SUMMARY OF timezone spoofs, potentially adversarial timezones, and non-work purpose-built accounts.

        This calculation is weighted differently from the adversarial components query, since both the timezones and non-work purpose-built accounts
        are only *potentially* adversarial.  Timezone spoofing requires intent to misrepresent location data, so it is weighted the most heavily.
        Potentially adversarial timezones and non-work purpose-built accounts are looped into this final percentage only by 1/3.

        Returns the average of the timezone spoof percentage, potentially adversarial timezone percentage, and non-work purpose-built account percentage.
        """
        query_params = {"repo": repo}

        return ReagentResponse(self.session.get(f"{self.reagent_base_url}/foreign-adversarial/total", params=query_params))