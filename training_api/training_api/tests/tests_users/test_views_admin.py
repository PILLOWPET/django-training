from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User


class UserViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(
            username="test_user", password="test_password"
        )
        test_user_1.save()
        test_user_2 = User.objects.create_superuser(
            username="test_user_2", password="test_password_2"
        )
        test_user_2.save()

    def init_client(self, user):
        client = APIClient()
        if user == 0:
            return client
        if user == 1:
            response = client.post(
                "/token/", {"username": "test_user", "password": "test_password"}
            )
        if user == 2:
            response = client.post(
                "/token/", {"username": "test_user_2", "password": "test_password_2"}
            )
        self.assertEqual(response.status_code, 200)
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION="jwt " + token)
        return client

    def test_change_other(self):
        client = self.init_client(2)
        response = client.patch(
            "/users/1/", {"email": "new_email@email.com"}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_other(self):
        client = self.init_client(2)
        response = client.delete("/users/1/")
        self.assertEqual(response.status_code, 204)
