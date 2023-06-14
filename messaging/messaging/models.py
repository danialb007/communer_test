from urllib import request

from django import models

from user.user.models import User


class Message(User):
    from_ = models.ForeignKey("User", on_delete=models.CASCADE)
    to = models.ForeignKey("User", on_delete=models.CASCADE)
    data = models.CharField(max_length=50)
