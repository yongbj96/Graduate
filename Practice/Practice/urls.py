"""Practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hello import views as hello
from member import views as member

from django.conf.urls import url, include
from rest_framework import routers
from users import views as users

router = routers.DefaultRouter()
router.register(r'users', users.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello.hi),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('member/', include('member.urls')), # member.urls에 들어오는 url들을 해당 파일에서 관리
]