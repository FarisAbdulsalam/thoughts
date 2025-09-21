from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import BlogUpdateView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView

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
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/', BlogUpdateView.as_view(), name='edit_blog'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
]
