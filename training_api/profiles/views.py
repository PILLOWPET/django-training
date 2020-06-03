from rest_framework import viewsets
from .models import Profile
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS
from .serializers import ProfileSerializer
from .permissions import ownProfile, IsValidAction

# Create your views here.


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [ownProfile & IsValidAction]
        return [permission() for permission in permission_classes]
