from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.select_related("author").order_by("created_at")
    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments},
    )


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


@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content,
            )

    return redirect("post_detail", pk=post.pk)


@login_required
def comment_delete(request, pk, comment_pk):
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk, post=post)

    if comment.author != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("삭제 권한이 없습니다.")

    if request.method == "POST":
        comment.delete()

    return redirect("post_detail", pk=post.pk)