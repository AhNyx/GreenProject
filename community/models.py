from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):   # 포스트 모델
    title = models.CharField(max_length=200)    # 제목: Char필드는 제한필요(최대=한글100자)
    content = models.TextField()                # 내용
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이: FK, User모델에서 가져옴 삭제연동
    create_date = models.DateTimeField(auto_now_add=True)       # 생성일: 최초 생성시 자동생성 수정시 변경안됨
    views = models.IntegerField(default=0)      # 조회수
    likes = models.IntegerField(default=0)      # 좋아요
