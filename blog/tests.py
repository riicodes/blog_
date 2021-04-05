from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Post


class PostListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser', password='banana', email='test@test.com')
        self.post = Post.objects.create(title="rinisha", author=self.user, body="is the best")

    def test_post(self):
        self.assertEqual(f'{self.post.title}', 'rinisha')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'is the best')

    def test_post_create_view(self):  # new
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id,
        })

        self.assertEqual(response.status_code, 302)
