import json

import requests

from recommendation.recommendation.models import ProcessedHealthData
from recommendation.recommendation.notification import send_obesity_notification
from recommendation.recommendation.serializer import ProcessedHealthDataSerializer


class ML:
    def __init__(self) -> None:
        # Setup
        # Do stuff before actual calculations and recommendations
        pass

    def get_users_data(self):
        data = requests.get("HEALTHSERVICE/users_health_data")
        self.process(json.loads(data))

    def process(data: dict):
        # Run ml algorithems
        # ...

        # Send notifications if neccessary
        bmi_is_high = True  # base on ai results
        if bmi_is_high:
            send_obesity_notification(user=data["user"])

        # Store data for further calculations
        serializer = ProcessedHealthDataSerializer(data=data)
        ProcessedHealthData.objects.create(**serializer.data)
