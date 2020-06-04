from django.test import TestCase

from django.contrib.auth.models import User


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(
            username="test_user", password="test_password"
        )
        test_user_1.save()

    def test_logged_in(self):
        url = "/token/"
        resp = self.client.post(
            url, {"username": "test_user", "password": "test_password"}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("token" in resp.data)

    def test_create(self):
        url = "/users/"
        resp = self.client.post(
            url, {"username": "test_user2", "password": "test_password2"}
        )
        self.assertEqual(resp.status_code, 201)
        self.assertTrue("username" in resp.data)
