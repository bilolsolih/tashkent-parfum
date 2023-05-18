from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "is_staff",
            "is_active",
            "is_superuser",
            "groups",
            "last_login",
            "user_permissions",
        ]
