from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from posts.models import Post


class PostViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(
            username="test_user", password="test_password"
        )
        test_user_1.save()
        Post.objects.create(
            title="test_title", content="test_content", user=test_user_1
        )

    def test_retrieve(self):
        url = "/posts/1/"
        resp = self.client.get(url)
        self.assertTrue(resp.status_code, 200)
        self.assertTrue("title" in resp.data)

    def test_list(self):
        url = "/posts/"
        resp = self.client.get(url)
        self.assertTrue(resp.status_code, 200)
        self.assertGreater(len(resp.data), 0)
        self.assertTrue("title" in resp.data[0])
