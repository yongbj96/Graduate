# 기본동작 관련
from django.contrib import admin
from django.urls import path
from Main import views as main
from member import views as member

# rest_framework, router 관련
from django.conf.urls import url, include
from rest_framework import routers
from users import views as users

# jwt 관련 (링크: https://dev-yakuza.posstree.com/ko/django/jwt/)
# obtain: JWT 토큰을 발행할 때 사용
# verify: JWT 토큰을 검증할 때 사용
# refresh: JWT 토큰을 갱신할 때 사용
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', users.UserViewSet) # users 페이지

urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지
    # id : yong, pw : tndlf123
    
    # 메인 페이지
    path('', main.login), # 메인 페이지

    # rest_framework 실습
    url(r'^', include(router.urls)), # users의 router
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # user 상세 페이지
    
    # GET, POST 실습
    path('member/', include('member.urls')), # member/~를 member/urls파일에서 관리

    # JWT 실습
    path('api/token/', obtain_jwt_token), #발행
    path('api/token/verify/', verify_jwt_token), #검증
    path('api/token/refresh/', refresh_jwt_token), #갱신

    # JWT 실습 - URL 연결 (‘api/blog/’,~)
]

# 중간일정 (대기)
# 두 개의 테이블 JOIN해서 GET 페이지 완성하기
## 정석 방법: https://wave1994.tistory.com/70
## 정석 방법: https://jay-ji.tistory.com/35
## 정석 마지막: https://jupiny.tistory.com/entry/selectrelated%EC%99%80-prefetchrelated
## Query 사용하는 방법: https://stackoverflow.com/questions/19590483/django-queryset-join-without-foreignkey
## 역참조: https://velog.io/@hwang-eunji/backend-django-%EC%97%AD%EC%B0%B8%EC%A1%B0-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0