from ai_proofreading_tool.ai_services.base_ai_service import BaseAIService
import anthropic

class ClaudeService(BaseAIService):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = anthropic.Client(api_key=self.api_key)

    def generate_suggestion(self, prompt: str, content: str) -> str:
        response = self.client.completion(
            prompt=f"{anthropic.HUMAN_PROMPT} {prompt}\n\n{content}{anthropic.AI_PROMPT}",
            model="claude-v1",
            max_tokens_to_sample=150,
            stop_sequences=[anthropic.HUMAN_PROMPT],
        )
        return response.completion