from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=95, help_text="Maximum 95 characters", db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    content = RichTextField(max_length=5000, blank=True, null=True, help_text="Maximum 5000 characters")
    status = models.IntegerField(choices=STATUS, default=1)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = CloudinaryField('image', default='placeholder')
    role = models.CharField(max_length=20, choices=(('Activist', 'Activist'), ('Volunteer', 'Volunteer'), ('Organization', 'Organization')), default='volunteer')

    def __str__(self):
        return self.user.username
    

class Region(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image', default='placeholder')
    image2 = CloudinaryField('image2', default='placeholder')
    image3 = CloudinaryField('image3', default='placeholder')
    image4 = CloudinaryField('image4', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.name