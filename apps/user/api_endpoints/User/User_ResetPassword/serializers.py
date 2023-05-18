from rest_framework import serializers


class UserResetPasswordSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=128)
    phone_number = serializers.CharField(max_length=15, min_length=9)
    device_id = serializers.CharField(max_length=50)
