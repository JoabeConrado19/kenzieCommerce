from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_superuser"):
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        have_password = validated_data.get("password")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if have_password:
            instance.set_password(validated_data["password"])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "cpf",
            "is_superuser",
            "is_seller",
        ]
        extra_kwargs = {"password": {"write_only": True}}
