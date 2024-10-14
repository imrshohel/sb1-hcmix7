from ai_proofreading_tool.database.user_model import UserModel

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def update_ai_service(self, service_name):
        return self.user_model.update_ai_service(service_name)

    def save_api_key(self, api_key):
        return self.user_model.save_api_key(api_key)

    def get_current_ai_service(self):
        return self.user_model.get_current_ai_service()

    def get_api_key(self):
        return self.user_model.get_api_key()