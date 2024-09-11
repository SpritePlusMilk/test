from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views

app_name = "core"

router = DefaultRouter()
router.register("products", views.ProductView, "products")

urlpatterns = [path("", views.MainPage.as_view())]
urlpatterns += router.urls
