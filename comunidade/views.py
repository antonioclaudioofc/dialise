from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment = Comment.objects.create(post=post, author=request.user, content=content)
            comment.save()
            return redirect('post_detail', pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            post = Post.objects.create(title=title, content=content, author=request.user)
            post.save()
            return redirect('post_list')
    return render(request, 'new_post.html')
