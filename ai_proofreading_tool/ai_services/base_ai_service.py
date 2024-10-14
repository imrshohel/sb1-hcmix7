from abc import ABC, abstractmethod

class BaseAIService(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def generate_suggestion(self, prompt: str, content: str) -> str:
        pass