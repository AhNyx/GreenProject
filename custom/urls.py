from django.urls import path
from . import views

app_name = 'custom'

urlpatterns = [
    #http://127.0.0.1:8000/custom/
    path("", views.main, name='main'),
    #qna list
    path("qnalist/", views.qnalist, name='qnalist'),
    path("qnalist2/", views.qnalist2, name='qnalist2'),
    path("qnalist3/", views.qnalist3, name='qnalist3'),

]
