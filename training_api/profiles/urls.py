from rest_framework import routers
from profiles import views

router = routers.DefaultRouter()
router.register(r"follow", views.FollowAPIView)
router.register(r"", views.ProfileAPIView)

urlpatterns = router.urls
