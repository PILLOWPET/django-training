from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import ReadOnly, ownPostChange
from .serializers import PostSerializer

# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [ownPostChange | ReadOnly]
