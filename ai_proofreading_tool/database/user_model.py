import sqlite3
import os
from typing import Optional

class UserModel:
    def __init__(self):
        self.db_path = os.path.join('resources', 'proofreading_tool.db')

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def update_ai_service(self, service_name: str) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE user_settings SET value = ? WHERE key = 'current_ai_service'", (service_name,))
            conn.commit()
            return cursor.rowcount > 0

    def save_api_key(self, api_key: str) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE user_settings SET value = ? WHERE key = 'api_key'", (api_key,))
            conn.commit()
            return cursor.rowcount > 0

    def get_current_ai_service(self) -> Optional[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM user_settings WHERE key = 'current_ai_service'")
            result = cursor.fetchone()
            return result[0] if result else None

    def get_api_key(self) -> Optional[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM user_settings WHERE key = 'api_key'")
            result = cursor.fetchone()
            return result[0] if result else None