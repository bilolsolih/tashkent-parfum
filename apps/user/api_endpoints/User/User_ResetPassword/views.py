from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User
from apps.verification.verification import send_code
from .serializers import UserResetPasswordSendCodeSerializer, UserResetPasswordSerializer


class UserResetPasswordSendCodeAPIView(APIView):
    @swagger_auto_schema(request_body=UserResetPasswordSendCodeSerializer)
    def post(self, request):
        serializer = UserResetPasswordSendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_code(serializer, code_type="res")
        return Response({"message": "Password reset verification code sent successfully."}, status=status.HTTP_200_OK)


class UserResetPasswordAPIView(APIView):
    @swagger_auto_schema(request_body=UserResetPasswordSerializer)
    def post(self, request):
        serializer = UserResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        phone_number = cd['phone_number']
        password1 = cd['password1']
        password2 = cd['password2']

        if password1 != password2:
            raise ValidationError('Passwords do not match')

        user = get_object_or_404(
            User,
            phone_number=phone_number,
            allowed_to_reset=True,
            is_active=True,
            is_deleted=False,
            is_verified=True
        )
        user.set_password(password1)
        user.allowed_to_reset = False
        user.save()
        return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)


__all__ = ["UserResetPasswordSendCodeAPIView", "UserResetPasswordAPIView"]
