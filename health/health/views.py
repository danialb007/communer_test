import json

from rest_framework import response, views

from health.health.models import HealthData
from health.health.serializer import HealthDataSerializer


class UserHealthData(views.APIView):
    def patch(self, request):
        data = request.data
        health_data, created = HealthData.objects.get_or_create(user=request.user)
        serializer = HealthDataSerializer(data=data)
        health_data.update(serializer.data)
        return response.Response({"message": "data updated successfully"})


class UsersHealthData(views.APIView):
    def get(self, request):
        health_data = HealthData.objects.all()
        serializer = HealthDataSerializer(health_data, many=True)
        return response.Response({"data": serializer.data})
