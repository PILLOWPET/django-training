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

    def test_get_comment_unauthenticated(self):
        client = APIClient()
        resp = client.get("/posts/1/comments/")
        self.assertEqual(resp.status_code, 200)
        self.assertGreater(len(resp.data), 0)
        self.assertTrue("content" in resp.data[0])

    def test_post_comment_unauthenticated(self):
        client = APIClient()
        resp = client.post(
            "/posts/1/comments/", {"content": "test_content"}, format="json"
        )
        self.assertEqual(resp.status_code, 401)

    def test_post_comment_own_post(self):
        client = APIClient()
        response = client.post(
            "/token/", {"username": "test_user", "password": "test_password"}
        )
        self.assertEqual(response.status_code, 200)
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION="jwt " + token)
        response = client.post(
            "/posts/1/comments/", {"content": "test_comment"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["date"])

    def test_post_comment_other_user_post(self):
        client = APIClient()
        response = client.post(
            "/token/", {"username": "test_user_2", "password": "test_password_2"}
        )
        self.assertEqual(response.status_code, 200)
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION="jwt " + token)
        response = client.post(
            "/posts/1/comments/", {"content": "test_comment"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["date"])
