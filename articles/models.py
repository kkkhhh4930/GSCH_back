from django.db import models
from django.conf import settings

# 게시글 모델
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 작성자 (사용자 모델과의 관계)
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일자 (자동으로 현재 날짜 및 시간 설정)
    updated_at = models.DateTimeField(auto_now=True)  # 수정일자 (자동으로 현재 날짜 및 시간 설정)

# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 작성자 (사용자 모델과의 관계)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 해당 댓글이 속한 게시글 (게시글 모델과의 관계)
    content = models.TextField(blank=False)  # 내용 (공백 허용 안 함)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일자 (자동으로 현재 날짜 및 시간 설정)
    updated_at = models.DateTimeField(auto_now=True)  # 수정일자 (자동으로 현재 날짜 및 시간 설정)