from django.conf.urls.static import static

from django.urls import path
from django.conf import settings

from . import views

app_name = 'price'

urlpatterns = [
    path(r'^barcodereader/$',views.barcodereader,name='barcodereader'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

'''
    path('', views.checkbookprice, name='checkbookprice'),
    path('setting', views.settingbarcode, name='settingbarcode'),
    path('<int:image_id>', views.BarcodeReader, name='barcodereader'),
''',