from django.contrib.auth.models import User
from django.db import models

# help 포스트 - Q&A게시판
class Help(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # 제목: Char필드는 제한필요(최대=한글100자)
    content = models.TextField()              #내용
    pub_date = models.DateTimeField(auto_now_add=True)         #발행일 자동
    modify_date = models.DateTimeField(null=True, blank=True) #입력 폼이 비어도 됨 수동일 생성
    views = models.IntegerField(default=0)  # 조회수

    def __str__(self):
        return self.title

# noc 포스트 - notice 공지사항게시판
# class Help(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)  # 제목: Char필드는 제한필요(최대=한글100자)
#     content = models.TextField()              #내용
#     pub_date = models.DateTimeField(auto_now_add=True)         #발행일 자동
#     modify_date = models.DateTimeField(null=True, blank=True) #입력 폼이 비어도 됨 수동일 생성
#     views = models.IntegerField(default=0)  # 조회수
#
#     def __str__(self):
#         return self.title



