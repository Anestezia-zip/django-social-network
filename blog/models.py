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
    replies = models.ForeignKey('self', null=True, blank=True, related_name='reply_to', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    

