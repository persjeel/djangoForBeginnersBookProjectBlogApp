# package to reference our active User
from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        # we add a sample blog post to test
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        # check if post contains correct values
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        # check if homepage returns a 200 HTTP status code
        self.assertEqual(response.status_code, 200)
        # check if homepage contains text of post
        self.assertContains(response, self.post.title)
        # check if homepage uses correct template
        self.assertTemplateUsed(response, 'home.html')
