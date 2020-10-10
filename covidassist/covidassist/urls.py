from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/auth/login/$', obtain_jwt_token, name='api-login'),
    url(r'^api/', include(router.urls))
]
