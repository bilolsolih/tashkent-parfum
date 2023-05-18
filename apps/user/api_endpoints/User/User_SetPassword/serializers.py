from rest_framework import serializers


class UserSetPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, min_length=9)
    device_id = serializers.CharField(max_length=50)
    password1 = serializers.CharField(max_length=128, min_length=8)
    password2 = serializers.CharField(max_length=128, min_length=8)
