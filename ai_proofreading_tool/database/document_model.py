import sqlite3
import os
from typing import List, Optional

class Document:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

class DocumentModel:
    def __init__(self):
        self.db_path = os.path.join('resources', 'proofreading_tool.db')

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def get_all_documents(self) -> List[Document]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, content FROM documents")
            return [Document(*row) for row in cursor.fetchall()]

    def get_document(self, document_id: int) -> Optional[Document]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, content FROM documents WHERE id = ?", (document_id,))
            result = cursor.fetchone()
            return Document(*result) if result else None

    def create_document(self, title: str, content: str = "") -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO documents (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
            return cursor.lastrowid

    def update_document(self, document_id: int, content: str) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE documents SET content = ? WHERE id = ?", (content, document_id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_document(self, document_id: int) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM documents WHERE id = ?", (document_id,))
            conn.commit()
            return cursor.rowcount > 0