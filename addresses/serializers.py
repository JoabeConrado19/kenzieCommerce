from rest_framework import serializers
from .models import Address
from rest_framework.exceptions import ValidationError


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        user = self.context["request"].user
        if Address.objects.filter(user=user, **validated_data).exists():
            raise ValidationError(
                {
                    "message": "Já existe um endereço com as mesmas informações para este usuário."
                }
            )
        validated_data["user"] = user
        return Address.objects.create(**validated_data)

    def update(self, instance: Address, validated_data: dict) -> Address:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = Address
        fields = [
            "id",
            "city",
            "neighborhood",
            "street",
            "state",
            "number",
            "user",
        ]
        read_only_fields = ["user"]
