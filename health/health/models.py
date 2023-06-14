from django import models

from health.health.notification import send_ideal_bmi_notification


class HealthData(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    heart_rate = models.IntegerField()
    bmi = models.IntegerField()
    blood_pressure = models.CharField(max_length=50)()
    blood_sugar = models.IntegerField()

    def update_data(self, data: dict):
        self.heart_rate = data["heart_rate"]
        self.bmi = data["bmi"]
        self.blood_pressure = data["blood_pressure"]
        self.blood_sugar = data["blood_sugar"]
        ideal = 120
        self.save()
        if self.bmi == ideal:
            send_ideal_bmi_notification(self.user)
