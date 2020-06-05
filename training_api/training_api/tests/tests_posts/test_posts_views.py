from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from posts.models import Post, Comment


class PostViewSetTest(APITestCase):
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
        post_1 = Post.objects.create(
            title="test_title", content="test_content", user=test_user_1
        )
        post_1.save()
        comment_1 = Comment.objects.create(
            content="test", user=test_user_1, post=post_1
        )
        comment_1.save()

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

    def test_retrieve_unauthenticated(self):
        client = self.init_client(0)
        resp = client.get("/posts/1/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("title" in resp.data)

    def test_list_unauthenticated(self):
        client = self.init_client(0)
        resp = client.get("/posts/")
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.data), 0)
        self.assertTrue("title" in resp.data[0])

    def test_create_unauthenticated(self):
        client = self.init_client(0)
        response = client.post(
            "/posts/", {"title": "test_title", "content": "test_content"}, format="json"
        )
        self.assertEqual(response.status_code, 401)

    def test_create_authenticated(self):
        client = self.init_client(1)
        response = client.post(
            "/posts/", {"title": "test_title", "content": "test_content"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["date"])

    def test_change_own_post(self):
        client = self.init_client(1)
        response = client.patch(
            "/posts/1/", {"title": "different_title"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "different_title")

    def test_change_other_user_post(self):
        client = self.init_client(2)
        response = client.patch(
            "/posts/1/", {"title": "different_title"}, format="json"
        )
        self.assertEqual(response.status_code, 403)

    def test_delete_own_post(self):
        client = self.init_client(1)
        response = client.delete("/posts/1/")
        self.assertEqual(response.status_code, 204)
        response_after_delete = client.get("/posts/1/")
        self.assertEqual(response_after_delete.status_code, 404)

    def test_delete_other_user_post(self):
        client = self.init_client(2)
        response = client.delete("/posts/1/", format="json")
        self.assertEqual(response.status_code, 403)
