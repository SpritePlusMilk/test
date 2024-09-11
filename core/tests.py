from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from random import randint

from core import factories, models, serializers


def create_product_data() -> dict:
    temp_object = factories.Product()
    data = serializers.Product(temp_object).data
    data.pop("id")
    models.Product.objects.get(id=temp_object.id).delete()

    return data


class TestProduct(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        for i in range(randint(3, 5)):
            factories.Product()
        self.initial_product_count = models.Product.objects.count()

    def test_list(self) -> None:
        url = reverse("core:products-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"{response.data = }")
        self.assertEqual(len(response.data), self.initial_product_count)

    def test_create(self) -> None:
        url = reverse("core:products-list")
        data = create_product_data()

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Product.objects.count(), self.initial_product_count + 1)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["description"], data["description"])
        self.assertEqual(response.data["cost"], data["cost"])
