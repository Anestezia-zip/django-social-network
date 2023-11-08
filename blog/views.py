from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.views import generic
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
  

class PostDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        print(post.slug)


        return render(
            request,
            "post_detail.html",
            {
                'post': post
            }
        )

