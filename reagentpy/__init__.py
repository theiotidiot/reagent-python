from reagentpy.clients.community import CommunityClient
from reagentpy.clients.repo import RepoClient
from reagentpy.clients.user import UserClient
from reagentpy.clients.enrichments import EnrichmentsClient
from reagentpy.clients.commit import CommitClient
from reagentpy.clients.composite_scores import CompositeClient
from reagentpy.clients.generic import GenericClient
from reagentpy.visualizations.demo_visualizations import DemoVisClient
from reagentpy.visualizations.timezone_visualizations import TimezoneVisClient
from reagentpy.visualizations.boe_visualizations import BOEVisClient

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
    
    def demo_visualizations(self):
        return DemoVisClient()

    def timezone_visualizations(self):
        return TimezoneVisClient()
    
    def boe_visualizations(self):
        return BOEVisClient()
    
    def composite_scores(self):
        return CompositeClient()
    
    def status(self):
        return GenericClient().get("/status")
    