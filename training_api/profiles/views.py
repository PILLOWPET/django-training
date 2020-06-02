from rest_framework import viewsets
from .models import Profile
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ProfileSerializer

# Create your views here.


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        # need_authentication = ["retrieve", "list"]
        need_authentication = []
        if self.action in need_authentication:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
