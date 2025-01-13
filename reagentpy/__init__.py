from reagentpy.clients.community import CommunityClient
from reagentpy.clients.repo import RepoClient
from reagentpy.clients.user import UserClient
from reagentpy.clients.enrichments import EnrichmentsClient
from reagentpy.clients.commit import CommitClient
from reagentpy.clients.generic import GenericClient
from reagentpy.visualizations.demo_visualizations import DemoVis
from reagentpy.visualizations.timezone_visualizations import TimezoneVis

class Reagent:

    def __init__(self):
        pass

    def community(self):
        return CommunityClient()
    
    def repo(self):
        return RepoClient()
    
    def user(self):
        return UserClient()
    
    def enrichments(self):
        return EnrichmentsClient()
    
    def commit(self):
        return CommitClient()
    
    def status(self):
        return GenericClient().get("/status")
    
    def demo_visualizations(self) -> DemoVis:
        return DemoVis()

    def timezone_visualizations(self) -> TimezoneVis:
        return TimezoneVis()