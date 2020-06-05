from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User


class ProfileViewSetTest(APITestCase):
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
            "/profiles/1/", {"description": "new_description"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("description" in response.data)
        self.assertEqual(response.data["description"], "new_description")

    def test_delete_other(self):
        client = self.init_client(2)
        response = client.delete("/profiles/1/")
        self.assertEqual(response.status_code, 403)
