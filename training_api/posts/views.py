from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    SAFE_METHODS,
)
from .permissions import ReadOnlyCreateOrOwnPost
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method not in SAFE_METHODS:
            permission_classes = [ReadOnlyCreateOrOwnPost]
        return [permission() for permission in permission_classes]
