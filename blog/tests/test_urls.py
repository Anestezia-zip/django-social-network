from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import add_post, edit_post, delete_post
from blog.urls import urlpatterns
from django.contrib.auth.models import User
from blog.models import UserProfile, Post


class TestUrls(TestCase):

    def test_add_url_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func, add_post)

    def test_edit_url_resolves(self):
        url = reverse('edit', kwargs={'post_id': 1})  # Change 1 to a valid post ID
        self.assertEquals(resolve(url).func, edit_post)

    def test_delete_post_url_resolves(self):
        url = reverse('delete_post', kwargs={'post_id': 1})  # Change 1 to a valid post ID
        self.assertEquals(resolve(url).func, delete_post)

    def test_blog_urls_include(self):
        resolved = resolve('/').url_name
        self.assertEquals(resolved, 'home')

    def test_edit_profile_url(self):
        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func.__name__, 'edit_profile')

    def test_add_post_url(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.__name__, 'add_post')

    def test_edit_post_url(self):
        url = reverse('edit', kwargs={'post_id': 1})  # Change 1 to a valid post ID
        self.assertEquals(resolve(url).func.__name__, 'edit_post')

    def test_delete_post_url(self):
        url = reverse('delete_post', kwargs={'post_id': 1})  # Change 1 to a valid post ID
        self.assertEquals(resolve(url).func.__name__, 'delete_post')

    def test_donate_url(self):
        url = reverse('donate')
        self.assertEquals(resolve(url).func.__name__, 'donate')
