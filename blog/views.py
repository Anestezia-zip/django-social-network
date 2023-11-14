from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View, generic
from django.views.generic.detail import DetailView
from django.utils.text import slugify

from .models import Post, Region, UserProfile
from .forms import PostForm, UserProfileForm


class AllPostsView(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 6
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post'


class UserPostsView(View):
    template_name = 'profile.html'

    def get(self, request):
        user_profile, user_posts = self.get_user_data(request)
        return render(request, self.template_name, {'user_profile': user_profile, 'user_posts': user_posts})

    def get_user_data(self, request):
        if request.user.is_authenticated:
            user = request.user
            user_profile = UserProfile.objects.get_or_create(user=user)[0]
            user_posts = Post.objects.filter(author=user)
        else:
            user_profile = None
            user_posts = []
        return user_profile, user_posts


class EditProfileView(View):
    template_name = 'edit_profile.html'

    def get(self, request):
        user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        form = UserProfileForm(instance=user_profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})


class AddPostView(View):
    template_name = 'add_post.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = self.generate_unique_slug(post.title)
            post.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def generate_unique_slug(self, title):
        base_slug = slugify(title)
        slug = base_slug
        counter = 1

        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug


class EditPostView(View):
    template_name = 'edit_post.html'

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})


class DeletePostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('profile')


class AboutUsView(View):
    template_name = 'about_us.html'

    def get(self, request):
        return render(request, self.template_name)
