from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *




urlpatterns = [
    path('', views.index, name='index'),
    path("images", upload_file, name = "image_upload"),
    path("success", success, name = "success"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)