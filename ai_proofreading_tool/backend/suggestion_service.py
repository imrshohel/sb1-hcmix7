from ai_proofreading_tool.ai_services.ai_service_factory import AIServiceFactory
from ai_proofreading_tool.utils.prompt_factory import PromptFactory

class SuggestionService:
    def __init__(self):
        self.ai_service_factory = AIServiceFactory()
        self.prompt_factory = PromptFactory()

    def get_suggestions(self, document_id):
        # Get the document content
        document_content = self.get_document_content(document_id)
        
        # Get the current AI service
        ai_service = self.ai_service_factory.get_current_service()
        
        # Get the prompts
        grammar_prompt = self.prompt_factory.get_prompt('grammar_check')
        style_prompt = self.prompt_factory.get_prompt('style_improvement')
        
        # Generate suggestions
        grammar_suggestions = ai_service.generate_suggestion(grammar_prompt, document_content)
        style_suggestions = ai_service.generate_suggestion(style_prompt, document_content)
        
        return grammar_suggestions + style_suggestions

    def get_document_content(self, document_id):
        # This method should be implemented to retrieve the document content
        pass