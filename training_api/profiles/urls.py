from django.urls import path, include
from rest_framework import routers
from .views import ProfileAPIView, FollowAPIView
from profiles import views

router = routers.DefaultRouter()
router.register(r"follow", views.FollowAPIView)
router.register(r"", views.ProfileAPIView)

urlpatterns = router.urls
