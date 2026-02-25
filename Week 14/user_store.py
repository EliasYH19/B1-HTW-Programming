import json
import os

class UserStore:
    def __init__(self, file_path):
        """Constructor accepts the file_path for data storage[cite: 89, 93]."""
        self.file_path = file_path

    def load(self):
        """Returns a list of user dictionaries and handles FileNotFoundError[cite: 91, 96, 97]."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save(self, users):
        """Writes the list of users to the file as JSON[cite: 97, 100]."""
        with open(self.file_path, "w") as file:
            json.dump(users, file, indent=4)

    def find_by_id(self, user_id):
        """Returns a user dictionary matching the ID or None[cite: 98, 101]."""
        users = self.load()
        return next((u for u in users if u['id'] == user_id), None)

    def update_user(self, user_id, updated_data):
        """Updates a user by ID and returns a success status[cite: 119, 120]."""
        users = self.load()
        for u in users:
            if u['id'] == user_id:
                u.update(updated_data)
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        """Removes a user by ID and returns a success status[cite: 122, 123]."""
        users = self.load()
        initial_count = len(users)
        users = [u for u in users if u['id'] != user_id]
        if len(users) < initial_count:
            self.save(users)
            return True
        return False