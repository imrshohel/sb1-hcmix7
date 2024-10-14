from ai_proofreading_tool.ai_services.base_ai_service import BaseAIService
from google.cloud import aiplatform

class GoogleAIService(BaseAIService):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        aiplatform.init(project=self.api_key)

    def generate_suggestion(self, prompt: str, content: str) -> str:
        model = aiplatform.Model("text-bison@001")
        response = model.predict(instances=[f"{prompt}\n\n{content}"])
        return response.predictions[0]