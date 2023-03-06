from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        validated_data["user"] = self.context["request"].user
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
