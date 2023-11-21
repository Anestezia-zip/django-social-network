from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Region, UserProfile
from django.contrib.auth.models import User


class TestAllPostsView(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data to test the display of all posts
        for i in range(10):
            Post.objects.create(
                title=f'Test Post {i}',
                content=f'Test Content {i}',
                author=User.objects.create_user(
                    username=f'user{i}', password='testpassword'
                ),
                slug=f'test-post-{i}'
            )
        Region.objects.create(
            name='Test Region', description='Test Description')

    def test_all_posts_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue('posts_list' in response.context)
        self.assertEqual(len(response.context['posts_list']), 6)


class TestPostDetailView(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test post to check the detailed view
        cls.post = Post.objects.create(
            title='Test Post Detail',
            content='Test Content Detail',
            author=User.objects.create_user(
                username='testuser', password='testpassword'),
            slug='test-post-detail'
        )

    def test_post_detail_view(self):
        response = self.client.get(
            reverse('post_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertTrue('post' in response.context)
        self.assertEqual(response.context['post'].title, 'Test Post Detail')


class TestProfileViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', password='testpassword')
        cls.user_profile = UserProfile.objects.create(user=cls.user)

    def test_edit_profile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)

    def test_add_post(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_edit_post(self):
        post = Post.objects.create(
            title='Test Post', content='Test Content', author=self.user)
        response = self.client.get(reverse('edit', args=[post.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        post = Post.objects.create(
            title='Test Post', content='Test Content', author=self.user)
        response = self.client.get(reverse('delete_post', args=[post.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

    def test_donate(self):
        response = self.client.get(reverse('donate'))
        self.assertEqual(response.status_code, 200)


