from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


@login_required
def post_new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,
            content=content,
            created_at=timezone.now(),
            author=request.user,
        )
        return redirect("post_list")

    return render(request, "blog/post_new.html")


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("삭제 권한이 없습니다.")

    if request.method == "POST":
        post.delete()

    return redirect("post_list")
