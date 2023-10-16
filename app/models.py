from flask_login import UserMixin
from .firestore_service import get_user


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: User data
        """
        self.id = user_data.username
        self.password = user_data.password
        
    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)

        if user_doc:
            user_data_dict = user_doc.to_dict()
            if user_data_dict and 'password' in user_data_dict:
                user_data = UserData(
                    username=user_doc.id,
                    password=user_data_dict['password'])
                return UserModel(user_data)

        return None
        

        