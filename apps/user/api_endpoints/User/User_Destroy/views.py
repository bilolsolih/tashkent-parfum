from rest_framework.generics import DestroyAPIView

from apps.user.models import User
from apps.user.permissions import IsTheSameUser


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [IsTheSameUser]
    queryset = User.objects.all()


__all__ = ["UserDestroyAPIView"]
