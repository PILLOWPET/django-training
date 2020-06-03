from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("test_user", "test@test.com", "test_password")

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("username").verbose_name
        self.assertEquals(field_label, "username")

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("email").verbose_name
        self.assertEquals(field_label, "email address")

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("password").verbose_name
        self.assertEquals(field_label, "password")

    def test_object_name(self):
        user = User.objects.get(id=1)
        self.assertEquals("test_user", str(user))
