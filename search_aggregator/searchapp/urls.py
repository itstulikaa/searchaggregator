from django.contrib import admin
from django.urls import path
from .views import searchaggview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',searchaggview) 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)