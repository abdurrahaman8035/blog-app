from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    """Test all functionalities related to blog view"""

    def setUp(self):
        """First function to run before any tests"""

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A nice blog post',
            author=self.user,
            body='Nice body content'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_body_content(self):
        self.assertEqual(f'{self.post.title}', 'A nice blog post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A nice blog post')
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_blog_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A nice blog post')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New Title',
            'body': 'New Body Content',
            'author': self.user.id,
        })
        # Check if response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New Title')
        self.assertEqual(Post.objects.last().body, 'New Body Content')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated Title',
            'body': 'Updated Body'
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
