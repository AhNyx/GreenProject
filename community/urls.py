from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name='community'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('write/', views.post_create, name='post_form'),
]
