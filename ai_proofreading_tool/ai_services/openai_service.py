from ai_proofreading_tool.ai_services.base_ai_service import BaseAIService
import openai

class OpenAIService(BaseAIService):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        openai.api_key = self.api_key

    def generate_suggestion(self, prompt: str, content: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{prompt}\n\n{content}",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()