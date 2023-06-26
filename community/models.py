from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)     # 카테고리 이름 - 중복불가
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)    # url과 연동, 중복불가, 유니코드(한글포함)가능

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f'/community/category/{self.slug}'   # 카테고리에 해당하는 절대 slug형 url을 반환
        return reverse('community:cate_page', args=[self.slug])     # reverse 방식으로 변경

    class Meta:     # 중첩모델
        verbose_name = 'category'
        verbose_name_plural = 'categories'  # 복수형 단어 직접 지정


class Post(models.Model):   # 포스트 모델
    title = models.CharField(max_length=200)    # 제목: Char필드는 제한필요(최대=한글100자)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이: FK, User모델에서 가져옴 삭제연동
    create_date = models.DateTimeField(auto_now_add=True)       # 생성일: 최초 생성시 자동생성, 수정시 변경안됨
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정일: 수동생성(null/공백 가능)
    views = models.PositiveIntegerField(default=0)      # 조회수 - 양수만 입력가능하도록 positive 추가
    # 카테고리: FK(null/공백 가능, 삭제비연동)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # 포스트추천인: 1사용자 - 여러 포스트 추천, 1포스트 - 여러 사용자의 추천 연결이 가능하도록 다대다필드
    liked_user = models.ManyToManyField(User, related_name='likes', blank=True)
    # 편집기 연결: 내용과 파일첨부를 대체
    description = RichTextUploadingField()

    def __str__(self):
        return self.title   # Post를 식별할 상황에서 기본인 id가 아니라 title값을 불러와줘서 알아보기 쉽게 함

    # 조회수 증가: 주훈씨 모델링 참고함. @property: 메서드를 속성처럼 사용할 수 있도록 해주는 데코레이터
    @property
    def update_views(self):
        self.views += 1
        self.save()
        return self.views

    # 포스트의 추천인 수
    def count_liked_user(self):
        return self.liked_user.count()
