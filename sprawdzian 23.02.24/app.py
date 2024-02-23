from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)

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

user_service = UserService()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    if user_data:
        if 'firstName' in user_data and 'lastName' in user_data and 'birthYear' in user_data and 'group' in user_data:
            user = user_service.create_user(user_data)
            return jsonify(user), 201
    return jsonify({'message': 'Invalid user data'}), 400

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.json
    if user_data:
        user = user_service.update_user(user_id, user_data)
        if user:
            return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_service.delete_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
