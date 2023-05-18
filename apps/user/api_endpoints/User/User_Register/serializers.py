from rest_framework import serializers

from apps.user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["full_name", "phone_number", "device_id"]
