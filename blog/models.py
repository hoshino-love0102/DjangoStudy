from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # 글 제목
    content = models.TextField()  # 글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일

    def __str__(self):
        return self.title