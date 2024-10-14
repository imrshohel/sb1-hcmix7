from ai_proofreading_tool.ai_services.base_ai_service import BaseAIService
import requests

class GroqService(BaseAIService):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.api_url = "https://api.groq.com/v1/completions"

    def generate_suggestion(self, prompt: str, content: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mixtral-8x7b-32768",
            "prompt": f"{prompt}\n\n{content}",
            "max_tokens": 150,
            "temperature": 0.5
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()["choices"][0]["text"].strip()