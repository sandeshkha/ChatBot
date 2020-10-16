class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anynomys(self):
        return Flase

    def get_id(self):
        return self.username
