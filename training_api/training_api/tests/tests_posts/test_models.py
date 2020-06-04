from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post, Comment


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="test_user", password="test_password")
        post = Post.objects.create(
            title="test_title", content="test_content", user=user
        )
        Comment.objects.create(user=user, post=post, content="test_content")

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), "test_title")
        self.assertIsNotNone(post.date)

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), "test_content")
        self.assertIsNotNone(comment.date)
