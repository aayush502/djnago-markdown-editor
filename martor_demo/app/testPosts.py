import imp
from turtle import pos
from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Docker", description="learning docker", wiki="containerization")
        self.assertEqual(post.title, "Docker")
        self.assertEqual(post.description, "learning docker")
        self.assertEqual(post.wiki, "containerization")