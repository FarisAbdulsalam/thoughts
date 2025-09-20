from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/blog_index', views.blog_index, name='blog_index'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('accounts/signup/', views.sign_up, name='sign_up'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='registration/signin.html'), name='sign_in'),
    path('sign_out/', auth_views.LogoutView.as_view(), name='sign_out'),
]
