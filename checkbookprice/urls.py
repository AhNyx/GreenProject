from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from . import views

app_name = 'price'

urlpatterns = [
    path('', views.checkbookprice, name='checkbookprice'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)