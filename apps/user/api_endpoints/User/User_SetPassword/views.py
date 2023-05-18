from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User
from .serializers import UserSetPasswordSerializer


class UserSetPasswordAPIView(APIView):

    @swagger_auto_schema(request_body=UserSetPasswordSerializer)
    def post(self, request):
        serializer = UserSetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        password1 = cd['password1']
        password2 = cd['password2']
        if password1 != password2:
            raise ValidationError('Passwords do not match.')
        phone_number = cd['phone_number']
        user = get_object_or_404(User, phone_number=phone_number, is_verified=True, is_active=False)
        user.set_password(password1)
        user.is_active = True
        user.save()
        return Response({'message': 'Password set successfully.'}, status=status.HTTP_200_OK)


__all__ = ['UserSetPasswordAPIView']
