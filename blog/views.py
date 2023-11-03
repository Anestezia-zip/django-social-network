from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.auth.models import User
# from .forms import CommentForm


class UserPostListView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_list'
    paginate_by = 6

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['posts_list'] = queryset.order_by('-date_created')
        return context