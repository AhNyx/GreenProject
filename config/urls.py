from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from greenbooks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("gbook/mypage", views.mypage, name='mypage'),
    path('common/', include('common.urls')),
    path('community/', include('community.urls')),  # 커뮤니티
    path('tradebook/', include('tradebook.urls')),
    path('mypage/', include('mypage.urls')),
    path("goods/", include("goods.urls")),
    path('custom/', include('custom.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),   # 편집기
    path('price/', include('checkbookprice.urls')), # 바코드가격조회
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
