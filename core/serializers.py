from rest_framework.exceptions import APIException
from rest_framework.serializers import ModelSerializer, Serializer

from core import models


class Product(ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

    def validate(self: Serializer, attrs: dict) -> dict:
        if not attrs["name"]:
            raise APIException("Имя является обязательным полем")

        if attrs["cost"] <= 0:
            raise APIException("Стоимость продукта не может быть отрицательной")

        return attrs
