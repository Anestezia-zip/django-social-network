from django.test import TestCase
from blog.forms import PostForm, UserProfileForm
from allauth.account.forms import SignupForm


class TestForms(TestCase):
    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Title',
            'content': 'Test content',
        })
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        # Check for number of errors expected
        self.assertEquals(len(form.errors), 2)

    def test_user_profile_form_valid_data(self):
        form = UserProfileForm(data={
            'bio': 'Test Bio',
            'avatar': '',
            'role': 'Volunteer'
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_no_data(self):
        form = UserProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_custom_signup_form_valid_data(self):
        form = SignupForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'user_type': 'Volunteer',
            'password1': 'testpassword123!',
            'password2': 'testpassword123!',
        })
        self.assertTrue(form.is_valid())

    def test_custom_signup_form_no_data(self):
        form = SignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
