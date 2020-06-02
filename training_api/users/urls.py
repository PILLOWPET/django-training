from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from users import views

router = routers.DefaultRouter()
router.register(r"", views.UserViewSet)

urlpatterns = [path("", include(router.urls))]
