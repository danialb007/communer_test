from rest_framework import response, views

from messaging.messaging.notification import send_notification
from messaging.messaging.serializer import MessageSerializer


class SendMessage(views.APIView):
    def post(self, request):
        data = request.data
        serializer = MessageSerializer(data=data)
        message = serializer.create()
        send_notification(from_=request.user, to=message.to, data=message.data)
        return response.Response({"message": "notification sent"})
