import time
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from blog.models import Post, Region, UserProfile


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post content.',
        )

    def test_post_creation(self):
        post = self.post
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)
        self.assertEqual(post.status, 1)  # Checking default status

    def test_post_update(self):
        post = self.post
        new_title = 'Updated Test Post'
        post.title = new_title
        time.sleep(1)
        post.save()
        self.assertGreater(post.date_updated, post.date_created)

    def test_post_ordering(self):
        # Create more posts with different date_created values
        Post.objects.create(
            title='Another Post',
            slug='another-post',
            author=self.user,
            content='Content for another post.',
            date_created=timezone.now() - timezone.timedelta(days=1)
        )
        Post.objects.create(
            title='Third Post',
            slug='third-post',
            author=self.user,
            content='Content for third post.',
            date_created=timezone.now() - timezone.timedelta(days=2)
        )

        # Check ordering
        posts = Post.objects.all()
        self.assertEqual(posts[0].title, 'Test Post')  # Latest post
        self.assertEqual(posts[1].title, 'Another Post')
        self.assertEqual(posts[2].title, 'Third Post')  # Oldest post

    def test_featured_image_default(self):
        post = self.post
        self.assertEqual(post.featured_image, 'placeholder')


class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.profile = UserProfile.objects.create(
            user=self.user,
            bio='Test bio for the user',
            role='Activist'
        )

    def test_profile_creation(self):
        profile = self.profile
        self.assertTrue(isinstance(profile, UserProfile))
        self.assertEqual(profile.__str__(), profile.user.username)

    def test_default_avatar(self):
        profile = self.profile
        self.assertEqual(
         profile.avatar,
         'https://res.cloudinary.com/dyadwedsy/image/upload/'
         'v1700328631/volunteer/anonym_nplen6.png'
        )

    def test_user_profile_relationship(self):
        profile = self.profile
        self.assertEqual(profile.user, self.user)

    def test_valid_role_choices(self):
        profile = self.profile
        valid_roles = [
            choice[0] for choice in UserProfile._meta.get_field('role').choices
        ]
        self.assertIn(profile.role, valid_roles)


class RegionModelTestCase(TestCase):
    def setUp(self):
        self.region = Region.objects.create(
            name='Test Region',
            description='Test description for the region'
        )

    def test_region_creation(self):
        region = self.region
        self.assertTrue(isinstance(region, Region))
        self.assertEqual(region.__str__(), region.name)

    def test_default_images(self):
        region = self.region
        self.assertEqual(region.image, 'placeholder')
        self.assertEqual(region.image2, 'placeholder')
        self.assertEqual(region.image3, 'placeholder')
        self.assertEqual(region.image4, 'placeholder')

    def test_region_description(self):
        region = self.region
        self.assertEqual(region.description, 'Test description for the region')

    def test_region_ordering(self):
        regions = Region.objects.all()
        self.assertEqual(list(regions), list(Region.objects.order_by("name")))
