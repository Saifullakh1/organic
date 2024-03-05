from rest_framework import serializers
from ..models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "email", "password"
        ]

    def create(self, data):
        return User.objects.create_user(**data)

