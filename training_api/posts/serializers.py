from rest_framework import serializers

from .models import Post

from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "user")
