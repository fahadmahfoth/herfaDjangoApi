
from django.contrib import admin
from django.urls import path , include
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view() ),
    url(r'^auth/', include('djoser.urls') ),
    url(r'^auth/', include('djoser.urls.authtoken') ),
    url(r'^auth/', include('djoser.urls.jwt') ),
]
