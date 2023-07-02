from django.urls import path
from . import views

app_name = 'custom'

urlpatterns = [
    # http://127.0.0.1:8000/custom/
    # qnalist (qna게시판)
    path("qnalist/", views.qnalist, name='qnalist'),
    path("qnalist2/", views.qnalist2, name='qnalist2'),
    path("qnalist3/", views.qnalist3, name='qnalist3'),

    # 1:1 게시판 - help
    path("help/list/", views.help_list, name='help_list'),  # 목록
    path('help/list/<int:help_id>/', views.help_view, name='help_view'),  # 상세 페이지
    path('help/write/', views.help_write, name='help_write'),  # 1:1상담 form 페이지
    path('help/modify/<int:help_id>/', views.help_modify, name='help_modify'),  # 1:1상담 수정
    path('help/delete/<int:help_id>/', views.help_delete, name='help_delete'),  # 글삭제
    path('help/answer/create/<int:help_id>/', views.help_answer, name='help_answer'),  # 답변 작성
    path('help/answer/modify/<int:help_id>/', views.answer_modify, name='answer_modify'),  # 답변 수정
    path('help/answer/delete/<int:help_id>/', views.answer_delete, name='answer_delete'),  # 답변 삭제


    # 공지사항
    path("notice/list/", views.notice_list, name='notice_list'),  # 공지목록
    path('notice/list/<int:notice_id>/', views.notice_view, name='notice_view'),  # 상세 페이지
    path('notice/write/', views.notice_write, name='notice_write'),  # 공지작성 페이지
    path('notice/modify/<int:notice_id>/', views.notice_modify, name='notice_modify'),  # 공지 수정
    path('notice/delete/<int:notice_id>/', views.notice_delete, name='notice_delete'),  # 공지사항삭제

]
