from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllPostsView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile/', views.UserPostsView.as_view(), name='profile'),
    path('profile/chat/<int:user_id>/', views.open_chat, name='open_chat'),
]