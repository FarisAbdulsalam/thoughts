from django.shortcuts import render, redirect
from .models import Blog, Post

# Create your views here.

def blog_index(request):
    blogs = Blog.objects.all()
    return render(request, "blog/blog_index.html", {"blogs": blogs})


def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        posts = blog.post_set.all()
    except Blog.DoesNotExist:
        return redirect("blog_list")

    return render(request, "blog/blog_detail.html", {"blog": blog, "posts": posts})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.all()
    except Post.DoesNotExist:
        return redirect("blog_list")

    return render(request, "blog/post_detail.html", {"post": post, "comments": comments})
