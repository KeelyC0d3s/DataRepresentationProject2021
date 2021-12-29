from model.user_details import UserDetails


class AuthenticatedUser:

    def __init__(self, user_details: UserDetails):
        self.id = str(user_details.id)
        self.name = user_details.name
        self.email_address = user_details.email_address
        self.username = user_details.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
