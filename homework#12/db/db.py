class UserDB:
    users = [{"name": "test", "email": "test@test.com", "password": "passhash"},
             {"name": "Bob", "email": "bob@test.com", "password": "passhash2"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def add(self, name, email, password_hash):
        # add check if user already exists
        for user in self.users:
            if user["email"] != email or user["name"] != name:
                user = {
                    "name": name,
                    "email": email,
                    "password": password_hash
                }
                self.users.append(user)
                return user
            return None

    def update_by_email(self, email, name, password):
        # TODO: refactor
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
            else:
                pass

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]
