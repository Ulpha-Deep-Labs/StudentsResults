from django.urls import path, include
# from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'results'

urlpatterns = [
    path('student/', include('django.contrib.auth.urls')),
    path('student/login/dashboard/', views.dashboard, name= 'dashboard'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
