from ai_proofreading_tool.ai_services.base_ai_service import BaseAIService
import requests

class OllamaService(BaseAIService):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.api_url = "http://localhost:11434/api/generate"

    def generate_suggestion(self, prompt: str, content: str) -> str:
        data = {
            "model": "llama2",
            "prompt": f"{prompt}\n\n{content}",
            "stream": False
        }
        response = requests.post(self.api_url, json=data)
        return response.json()["response"].strip()