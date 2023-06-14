from unittest.mock import patch

from django.test import TestCase

from health.models import HealthData
from user.user.models import User


class HealthDataTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.health_data = HealthData.objects.create(
            user=self.user,
            heart_rate=100,
            bmi="120/80",
            blood_pressure=20,
            blood_sugar=20,
        )

    def test_health_data_created(self):
        self.assertEqual(self.health_data.user_id, self.user.id)
        self.assertEqual(self.health_data.heart_rate, 80)
        self.assertEqual(self.health_data.blood_pressure, "120/80")
        self.assertEqual(self.health_data.weight, 65)
        self.assertEqual(self.health_data.height, 170)

    def test_get_health_data_by_patient_id(self):
        health_data = HealthData.objects.filter(user_id=self.user.id)
        self.assertEqual(len(health_data), 1)
        self.assertEqual(health_data[0].user_id, self.user.id)

    def test_health_data_update(self):
        new_data = {
            "heart_rate": 110,
            "bmi": 140,
            "blood_pressure": "110/70",
            "blood_sugar": 40,
        }
        self.health_data.update_data(new_data)

        self.assertEqual(self.health_data.heart_rate, new_data["heart_rate"])
        self.assertEqual(self.health_data.bmi, new_data["bmi"])
        self.assertEqual(self.health_data.blood_pressure, new_data["blood_pressure"])
        self.assertEqual(self.health_data.blood_sugar, new_data["blood_sugar"])

    @patch("notification.notification.utils.send_notification")
    def test_send_notification_when_bmi_is_120(self, mock_send_notification):
        new_data = {
            "bmi": 120,
        }
        self.health_data.update_data(new_data)
        mock_send_notification.assert_called_once()
