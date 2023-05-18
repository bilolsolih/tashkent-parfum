from rest_framework import serializers


class VerificationCodeVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, min_length=9)
    device_id = serializers.CharField(max_length=50)
    code = serializers.CharField(max_length=6, min_length=6)
    code_type = serializers.CharField(max_length=3, min_length=3)
