from django.contrib import admin
from django.test import TestCase
from blog.models import Post, Region, UserProfile


class TestAdmin(TestCase):
    def test_post_admin_registered(self):
        self.assertIn(Post, admin.site._registry)

    def test_region_admin_registered(self):
        self.assertIn(Region, admin.site._registry)

    def test_user_profile_admin_registered(self):
        self.assertIn(UserProfile, admin.site._registry)
