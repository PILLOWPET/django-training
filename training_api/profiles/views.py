from rest_framework import viewsets
from .models import Profile
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS
from .serializers import ProfileSerializer
from .permissions import ownProfile, IsValidAction
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ParseError
from shared.permissions import IsAdmin

# Create your views here.


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [ownProfile & IsValidAction | IsAdmin]
        return [permission() for permission in permission_classes]


class FollowAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [~AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            profile_id = request.data["id"]
        except KeyError:
            raise ParseError(detail="Profile id needs to be specified")
        try:
            profile_to_follow = Profile.objects.get(pk=profile_id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Profile not found")
        user_profile = request.user.profile
        user_profile.following_profiles.add(profile_to_follow)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        user_profile.save()
        return Response(serializer.data)
