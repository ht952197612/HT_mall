from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin


urlpatterns = [
    url(r'^login/$', obtain_jwt_token),   # 传统的登陆验证
]