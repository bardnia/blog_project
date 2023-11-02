from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Tag
from django.db.models import Q
from .forms import CommentForm

# 개시물 목록
def postlist(request):
    posts = Post.objects.all()
    return render(request, 'blog/postlist.html', {'posts':posts})

# 게시물 추가
def post_write(request):
    pass

# 현관문
def post_top(request):
    return render(request, 'blog/post_top.html')

# 개시물 상세
def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data['message']
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, 'blog/postdetail.html', {'post':post, 'form':form})

# 게시물 수정
def post_edit(request, pk):
    pass

# 게시물 제거
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'blog/post_delete.html', {'post': post})

# 태그 기능
def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'blog/postlist.html', {'posts':posts})