from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.auth.models import User
# from .forms import CommentForm


class UserPostListView(generic.ListView):
    model = Post
    template_name = 'user_posts.html'
    paginate_by = 6
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-date_created')
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form, *args, **kwargs):#
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'blog_post_detail'

    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)