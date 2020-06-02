from django.urls import path, include
from rest_framework import routers
from .views import ProfileAPIView
from profiles import views

router = routers.DefaultRouter()
router.register(r"", views.ProfileAPIView)

urlpatterns = [path("", include(router.urls))]
