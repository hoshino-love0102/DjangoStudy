from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_post_create(request):
    title = request.data.get("title")
    content = request.data.get("content")

    if not title or not content:
        return Response({"detail": "title, content는 필수입니다."}, status=status.HTTP_400_BAD_REQUEST)

    post = Post.objects.create(
        title=title,
        content=content,
        author=request.user,
    )
    return Response({"id": post.id}, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def api_post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user and not request.user.is_superuser:
        return Response({"detail": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
