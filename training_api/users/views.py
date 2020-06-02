from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        need_authentication = [
            "retrieve",
            "list",
            "update",
            "destroy",
            "partial_update",
        ]
        if self.action in need_authentication:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
