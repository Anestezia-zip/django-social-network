from django import forms
from .models import Post, UserProfile
from ckeditor.widgets import CKEditorWidget
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    USER_CHOICES = (
        ('Activist', 'Activist'),
        ('Volunteer', 'Volunteer'),
        ('Organization', 'Organization'),
    )
    
    user_type = forms.ChoiceField(choices=USER_CHOICES, label='Choose the role that suits you best')


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'role']