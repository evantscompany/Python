class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.todos = []

    def check_password(self, password):
        return self.password == password
