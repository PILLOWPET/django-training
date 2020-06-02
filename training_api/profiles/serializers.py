from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ("user", "description")
