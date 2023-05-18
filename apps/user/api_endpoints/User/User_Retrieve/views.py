from rest_framework.generics import RetrieveAPIView

from apps.user.models import User

from .serializers import UserRetrieveSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


__all__ = ["UserRetrieveAPIView"]
