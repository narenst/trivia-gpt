from triviagpt.services.openai import OpenAIService

def init(app):
    """
    Initialize all the services, if needed
    """
    OpenAIService.init(app)