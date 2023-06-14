from rest_framework import serializers

from messaging.messaging.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
