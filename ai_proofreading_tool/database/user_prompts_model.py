import sqlite3
import os
from typing import Dict, Optional

class UserPromptsModel:
    def __init__(self):
        self.db_path = os.path.join('resources', 'proofreading_tool.db')

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def get_all_user_prompts(self) -> Dict[str, str]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT prompt_name, prompt_content FROM user_prompts")
        results = cursor.fetchall()
        conn.close()
        return {row[0]: row[1] for row in results}

    def get_user_prompt(self, prompt_name: str) -> Optional[str]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT prompt_content FROM user_prompts WHERE prompt_name = ?", (prompt_name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def save_user_prompt(self, prompt_name: str, prompt_content: str) -> None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT OR REPLACE INTO user_prompts (prompt_name, prompt_content)
        VALUES (?, ?)
        ''', (prompt_name, prompt_content))
        conn.commit()
        conn.close()

    def delete_user_prompt(self, prompt_name: str) -> None:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_prompts WHERE prompt_name = ?", (prompt_name,))
        conn.commit()
        conn.close()