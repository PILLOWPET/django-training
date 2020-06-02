from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import ReadOnlyCreateOrOwnPost
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ReadOnlyCreateOrOwnPost]
