from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View, generic
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages


class AllPostsView(generic.ListView):
    model = Post
    template_name = 'home.html'
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


class UserPostsView(View):
    template_name = 'profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            user_posts = Post.objects.filter(author=user)
        else:
            user_posts = []  # empty list for unauthenticated users
        return render(request, self.template_name, {'user_posts': user_posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # Generate a unique slug based on the title
            base_slug = slugify(post.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            post.slug = slug
            post.save()
            return redirect('home')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('profile')


def open_chat(request, user_id):
    # Логика открытия чата, например, создание новой комнаты чата
    # ...
    return render(request, 'chat_room.html', {'user_id': user_id})