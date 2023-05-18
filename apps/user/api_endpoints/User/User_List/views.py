from rest_framework.generics import ListAPIView

from apps.user.models import User

from .serializers import UserListSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


__all__ = ["UserListAPIView"]
