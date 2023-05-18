from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from apps.user.models import User
from apps.user.permissions import IsTheSameUser

from .serializers import UserUpdateSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsTheSameUser]
    parser_classes = [MultiPartParser, FormParser]


__all__ = ["UserUpdateAPIView"]
