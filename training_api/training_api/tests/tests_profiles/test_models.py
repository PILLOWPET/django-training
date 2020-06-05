from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("test_user", "test@test.com", "test_password")

    def test_profile_description(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.description, "")

    def test_str(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(str(profile), "test_user")

    def test_photo(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.photo, "")
