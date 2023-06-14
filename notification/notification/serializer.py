from rest_framework import serializers

from notification.notification.models import Notifaction


class NotifactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifaction
