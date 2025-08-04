
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<int:article_id>', views.blog_details, name='blog_details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


