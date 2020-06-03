from rest_framework import viewsets, status
from .models import Post
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    SAFE_METHODS,
)
from .permissions import ReadOnlyCreateOrOwnPost
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        post = request.data
        post["user"] = request.user.id
        serializer = PostSerializer(data=post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        permission_classes = []
        if self.request.method not in SAFE_METHODS:
            permission_classes = [ReadOnlyCreateOrOwnPost]
        return [permission() for permission in permission_classes]
