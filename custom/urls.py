from django.urls import path
from . import views

app_name = 'custom'

urlpatterns = [
    #http://127.0.0.1:8000/custom/
    #qnalist (qna게시판)
    path("qnalist/", views.qnalist, name='qnalist'),
    path("qnalist2/", views.qnalist2, name='qnalist2'),
    path("qnalist3/", views.qnalist3, name='qnalist3'),

    #1:1 게시판 - help
    path("helplist", views.help_list, name='help_list'), #목록
    path('helplist/<int:help_id>/', views.help_view, name='help_view'),  #상세 페이지
    path('helpwrite/', views.help_write, name='help_write'),        # 1:1상담 form 페이지
    path('helpmodify/<int:help_id>/', views.help_modify, name='help_modify'),     # 1:1상담 수정

]
