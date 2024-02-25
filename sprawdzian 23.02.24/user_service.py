from typing import List, Dict

class UserService:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all_users(self) -> List[Dict]:
        return self.users

    def get_user_by_id(self, user_id: int) -> Dict:
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def create_user(self, user_data: Dict) -> Dict:
        user_data['id'] = self.next_id
        self.next_id += 1
        self.users.append(user_data)
        return user_data

    def update_user(self, user_id: int, new_data: Dict) -> Dict:
        for user in self.users:
            if user['id'] == user_id:
                user.update(new_data)
                return user
        return None

    def delete_user(self, user_id: int) -> Dict:
        for idx, user in enumerate(self.users):
            if user['id'] == user_id:
                return self.users.pop(idx)
        return None
