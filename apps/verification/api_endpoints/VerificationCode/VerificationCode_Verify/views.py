from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User
from apps.verification.models import VerificationCode
from .serializers import VerificationCodeVerifySerializer


class VerificationCodeVerifyAPIView(APIView):
    @swagger_auto_schema(request_body=VerificationCodeVerifySerializer)
    def post(self, request):
        serializer = VerificationCodeVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        phone_number = cd["phone_number"]
        device_id = cd["device_id"]
        code = cd["code"]
        code_type = cd['code_type']
        try:
            verification_code = VerificationCode.objects.get(
                phone_number=phone_number,
                device_id=device_id,
                code=code,
                code_type=code_type
            )
        except VerificationCode.DoesNotExist:
            return Response(
                {
                    "message": "Verification code for this number and device doesn't exist!"
                }, status=status.HTTP_404_NOT_FOUND,
            )
        if verification_code:
            if code_type == 'ver':
                user = get_object_or_404(User, phone_number=phone_number)
                user.is_verified = True
                user.save()
            elif code_type == 'res':
                user = get_object_or_404(
                    User,
                    phone_number=phone_number,
                    is_active=True,
                    is_deleted=False,
                    is_verified=True
                )
                user.allowed_to_reset = True
                user.save()
            else:
                raise ValueError('Code type is not provided or wrong!')
            verification_code.delete()
            return Response({"message": "Verified successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Failed to verify!"}, status=status.HTTP_400_BAD_REQUEST)


__all__ = ['VerificationCodeVerifyAPIView']
