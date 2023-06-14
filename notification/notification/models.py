from django import models


class Notifaction(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    sent_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)
