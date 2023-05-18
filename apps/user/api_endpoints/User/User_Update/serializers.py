from rest_framework import serializers

from apps.user.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "full_name"]
        # exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'last_login', 'user_permissions']
