from rest_framework import viewsets, status
from .models import Post
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    SAFE_METHODS,
)
from .permissions import ReadOnlyCreateOrOwnPost
from .serializers import PostSerializer
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


class PostFollowedAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [~AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Post.objects.all()
        followed_profiles = request.user.profile.following_profiles.all()
        filtered_qs = Post.objects.none()
        for profile in followed_profiles:
            filtered_qs = filtered_qs.union(queryset.filter(user=profile.user))
        serializer = PostSerializer(filtered_qs, many=True)
        return Response(serializer.data)
