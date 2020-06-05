from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User


class UserViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(
            username="test_user", password="test_password"
        )
        test_user_1.save()
        test_user_2 = User.objects.create_user(
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

    def test_logged_in(self):
        url = "/token/"
        resp = self.client.post(
            url, {"username": "test_user", "password": "test_password"}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("token" in resp.data)

    def test_create(self):
        client = self.init_client(0)
        resp = client.post(
            "/users/", {"username": "test_user2", "password": "test_password2"}
        )
        self.assertEqual(resp.status_code, 201)
        self.assertTrue("username" in resp.data)

    def test_list_unauthenticated(self):
        client = self.init_client(0)
        response = client.get("/users/")
        self.assertEqual(response.status_code, 401)

    def test_list_authenticated(self):
        client = self.init_client(1)
        response = client.get("/users/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)
        self.assertTrue("username" in response.data[0])

    def test_create_authenticated(self):
        client = self.init_client(1)
        response = client.post(
            "/users/",
            {"username": "test_user_3", "password": "test_password_3"},
            format="json",
        )
        self.assertEqual(response.status_code, 403)

    def test_change_own(self):
        client = self.init_client(1)
        response = client.patch(
            "/users/1/", {"email": "new_email@email.com"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("email" in response.data)

    def test_change_other(self):
        client = self.init_client(2)
        response = client.patch(
            "/users/1/", {"email": "new_email@email.com"}, format="json"
        )
        self.assertEqual(response.status_code, 403)

    def delete_own(self):
        client = self.init_client(1)
        response = client.delete("/users/1")
        self.assertEqual(response.status_code, 204)

    def delete_other(self):
        client = self.init_client(2)
        response = client.delete("/users/1/")
        self.assertEqual(response.status_code, 403)
