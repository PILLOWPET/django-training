from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PostSerializer

# Create your views here.


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        need_authentication = ["update", "create", "destroy", "partial_update"]
        if self.action in need_authentication:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
