import json

from rest_framework import response, views

from health.health.models import HealthData
from notification.notification.serializer import NotifactionSerializer
from notification.notification.utils import send_notification


class SendGeneral(views.APIView):
    def post(self, request):
        data = request.data
        serializer = NotifactionSerializer(data=data)
        notification = serializer.create()
        send_notification(notification)
        return response.Response({"message": "notification sent"})


class SendMessage(views.APIView):
    def post(self, request):
        data = request.data
        serializer = NotifactionSerializer(data=data)
        notification = serializer.create()
        send_notification(notification)
        return response.Response({"message": "notification sent"})
