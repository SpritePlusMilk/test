from django.views.generic import TemplateView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny


from core import models, serializers


class MainPage(TemplateView):
    template_name = 'main.html'


class ProductView(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.Product
    permission_classes = (AllowAny, )
