from urllib import request

from user.user.models import User


class Patient(User):
    def update_health_data(self, data):
        request.post("HEALTHSERVICE/user_health_data", data=data)
