from rest_framework import serializers
from .models import Reminders


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminders
        fields = "__all__"
