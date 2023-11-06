from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.UserPostListView.as_view(), name='home'),
    # path('posts/user/<str:username>', views.UserPostListView.as_view(), name='user_posts'),
]