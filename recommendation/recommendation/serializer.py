from rest_framework import serializers

from recommendation.recommendation.models import ProcessedHealthData


class ProcessedHealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedHealthData
