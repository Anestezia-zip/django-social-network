from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=95, help_text="Maximum 95 characters", db_index=True)
    content = RichTextField(max_length=5000, blank=True, null=True, help_text="Maximum 5000 characters")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    slug = models.SlugField(max_length=200, unique=True)
    likes = models.ManyToManyField(User, blank=True, related_name='blog_likes')
    replies = models.ForeignKey('self', null=True, blank=True, related_name='reply_to', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    # featured_image = CloudinaryField('image', default='placeholder')
    # excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = 'Create post'
        verbose_name_plural = 'Create posts'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()