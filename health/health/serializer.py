from rest_framework import serializers

from health.health.models import HealthData


class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
