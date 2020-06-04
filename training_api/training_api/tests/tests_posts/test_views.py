from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from posts.models import Post, Comment


class PostViewSetTest(TestCase):
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
