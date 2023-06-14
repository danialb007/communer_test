from django import models


class ProcessedHealthData(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    bmi = models.IntegerField()
    blood_pressure = models.IntegerField()
    blood_sugar = models.IntegerField()
