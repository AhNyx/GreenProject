from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name='community'),                            # post 리스트
    path('category/<str:slug>/', views.category_list, name='cate_list'),    # 카테고리리스트(slug기능)
    path('write/', views.post_create, name='post_create'),                  # post 작성
    path('<str:slug>/write/', views.cate_post_create, name='cate_post_create'),     # cate_post 작성
    path('<int:post_id>/', views.detail, name='detail'),                    # post_id로 상세보기
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),         # post 수정
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),   # post_id로 삭제
    path('<int:post_id>/reply/', views.reply_create, name='re_create'),     # 댓글 등록
    path('reply/<int:reply_id>/delete/', views.reply_delete, name='re_delete'),     # 댓글 삭제
    path('likes/', views.post_like, name='post_like'),  # 추천
]
