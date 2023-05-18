from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from apps.user.models import User
from apps.verification.verification import send_code
from .serializers import UserRegisterSerializer


class UserInitialRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        full_name = serializer.validated_data['full_name']
        phone_number = serializer.validated_data['phone_number']
        User.objects.create(full_name=full_name, phone_number=phone_number)
        send_code(serializer, code_type='ver')


__all__ = ["UserInitialRegisterAPIView"]
