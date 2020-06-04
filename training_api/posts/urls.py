from django.urls import path, include
from rest_framework import routers
from posts import views

router = routers.DefaultRouter()
router.register(r"followed", views.PostFollowedAPIView)
router.register(r"", views.PostAPIView)


urlpatterns = [path("", include(router.urls))]
