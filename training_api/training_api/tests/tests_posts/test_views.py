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
        post_1 = Post.objects.create(
            title="test_title", content="test_content", user=test_user_1
        )
        post_1.save()
        comment_1 = Comment.objects.create(
            content="test", user=test_user_1, post=post_1
        )
        comment_1.save()

    def test_retrieve(self):
        url = "/posts/1/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("title" in resp.data)

    def test_list(self):
        url = "/posts/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.data), 0)
        self.assertTrue("title" in resp.data[0])

    def test_comment(self):
        url = "/posts/1/comments/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.data), 0)
        self.assertTrue("content" in resp.data[0])

    def test_create_unauthenticated(self):
        client = APIClient()
        response = client.post(
            "/posts/", {"title": "test_title", "content": "test_content"}, format="json"
        )
        self.assertEqual(response.status_code, 401)

    def test_create_authenticated(self):
        client = APIClient()
        response = client.post(
            "/token/", {"username": "test_user", "password": "test_password"}
        )
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION="jwt " + token)
        response = client.post(
            "/posts/", {"title": "test_title", "content": "test_content"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["date"])
