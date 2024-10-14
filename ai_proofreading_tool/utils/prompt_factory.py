import json
import os
from typing import Dict, Any, List
from ai_proofreading_tool.database.user_prompts_model import UserPromptsModel

class PromptFactory:
    def __init__(self):
        self.default_prompts = self._load_default_prompts()
        self.user_prompts_model = UserPromptsModel()

    def _load_default_prompts(self) -> Dict[str, Any]:
        default_prompts_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'default_prompts.json')
        with open(default_prompts_path, 'r') as f:
            return json.load(f)

    def get_prompt(self, prompt_name: str) -> str:
        user_prompt = self.user_prompts_model.get_user_prompt(prompt_name)
        return user_prompt if user_prompt else self.default_prompts.get(prompt_name, '')

    def save_user_prompt(self, prompt_name: str, prompt_content: str) -> None:
        self.user_prompts_model.save_user_prompt(prompt_name, prompt_content)

    def reset_prompt(self, prompt_name: str) -> None:
        self.user_prompts_model.delete_user_prompt(prompt_name)

    def get_all_prompts(self) -> Dict[str, str]:
        all_prompts = self.default_prompts.copy()
        all_prompts.update(self.user_prompts_model.get_all_user_prompts())
        return all_prompts

    def get_prompt_categories(self) -> Dict[str, List[str]]:
        return {
            "Heavier Editing": ["Streamline", "Strong", "Improve", "Polish", "Rewrite"],
            "Change Tone": ["Academic", "Formal", "Casual", "Speech"],
            "Regions and Standards": ["UK", "MLA", "Chicago", "APA"],
            "Industry-specific": ["SEO", "Social", "Technical", "Legal", "Apply", "Thesis"],
            "Structure": ["List", "CV", "Concise", "Trim"]
        }