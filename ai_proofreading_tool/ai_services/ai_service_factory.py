from ai_proofreading_tool.ai_services.openai_service import OpenAIService
from ai_proofreading_tool.ai_services.claude_service import ClaudeService
from ai_proofreading_tool.ai_services.googleai_service import GoogleAIService
from ai_proofreading_tool.ai_services.groq_service import GroqService
from ai_proofreading_tool.ai_services.ollama_service import OllamaService
from ai_proofreading_tool.backend.user_service import UserService

class AIServiceFactory:
    def __init__(self):
        self.user_service = UserService()
        self.services = {
            'OpenAI': OpenAIService,
            'Claude AI': ClaudeService,
            'Google AI': GoogleAIService,
            'Groq': GroqService,
            'Ollama': OllamaService
        }

    def get_current_service(self):
        current_service_name = self.user_service.get_current_ai_service()
        api_key = self.user_service.get_api_key()
        
        if current_service_name in self.services:
            return self.services[current_service_name](api_key)
        else:
            raise ValueError(f"Unknown AI service: {current_service_name}")