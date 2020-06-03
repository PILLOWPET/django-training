from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="test_user", password="test_password")
        Post.objects.create(title="test_title", content="test_content", user=user)

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEquals(str(post), "test_title")
        self.assertIsNotNone(post.date)
