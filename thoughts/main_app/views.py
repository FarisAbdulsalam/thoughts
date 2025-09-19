from django.shortcuts import render, redirect
from .models import Blog, Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        content = request.POST.get("comment_content")
        if content:
            Comment.objects.create(
                user=request.user,
                post=post,
                comment_content=content
            )
        return redirect("post_detail", post_id=post.id)

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        post_id = comment.post.id
        comment.delete()
        return redirect("post_detail", post_id=post_id)
    
def sign_up(request):
  error_message=''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign-up, please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)