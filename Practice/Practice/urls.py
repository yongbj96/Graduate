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
router.register(r'users', users.UserViewSet) # users 페이지

urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지
    
    # 네비게이터 페이지
    path('', hello.hi), # 메인 페이지

    # resr_framework 실습
    url(r'^', include(router.urls)), # users의 router
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # user 상세 페이지
    
    # GET, POST 실습
    path('member/', include('member.urls')), # member/~를 member/urls파일에서 관리
]

# 중간일정
# 두 개의 테이블 JOIN해서 GET 페이지 완성하기
## 정석 방법: https://wave1994.tistory.com/70
## 정석 방법: https://jay-ji.tistory.com/35
## 정석 마지막: https://jupiny.tistory.com/entry/selectrelated%EC%99%80-prefetchrelated
## Query 사용하는 방법: https://stackoverflow.com/questions/19590483/django-queryset-join-without-foreignkey
## 역참조: https://velog.io/@hwang-eunji/backend-django-%EC%97%AD%EC%B0%B8%EC%A1%B0-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0