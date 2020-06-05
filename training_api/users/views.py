from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .permissions import NewUser, OwnUser
from shared.permissions import IsAdmin

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [NewUser | OwnUser | IsAdmin]
        return [permission() for permission in permission_classes]
