from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.verification.verification import send_code

from .serializers import UserResetPasswordSerializer


class UserResetPasswordSendCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserResetPasswordSerializer)
    def post(self, request):
        serializer = UserResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_code(serializer, code_type="res")
        return Response({"message": "Password set successfully."}, status=status.HTTP_200_OK)


__all__ = ["UserResetPasswordSendCodeAPIView"]
