from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllPostsView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile/', views.UserPostsView.as_view(), name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('about_us/', views.about_us, name='about_us'),
]
