from django.urls import path

from . import views

app_name = 'tradebook'

urlpatterns = [
    path('', views.tradebook_list, name='tradebook_list'),
]