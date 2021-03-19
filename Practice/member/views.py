from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BoardMember

# Post 추가
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated # 로그인여부 확인
from rest_framework_jwt.authentication import JSONWebTokenAuthentication # JWT인증 확인
from .models import Post

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username    = request.POST.get('username', None)
        password    = request.POST['password']
        email       = request.POST.get('email', None)

        res_data = {}
        if not (username and email):
            res_data['error'] = '모든 값을 입력해주세요.'
        else:
            member = BoardMember(
                username = username,
                password = password,
                email = email,
            )
            # member.save() # 데이터베이스에 저장
            print("#####회원가입#####\nid: ", member.username, "\npw: ", member.password, "\nemail: ", member.email)

        return redirect('/') # 다른 페이지로 이동

@api_view(['GET']) # 요청이 GET인지 확인하여 JSON 타입으로 반환
@permission_classes((IsAuthenticated, )) # 권한을 체크(로그인 했는지 여부만 체크)
@authentication_classes((JSONWebTokenAuthentication,)) # JWT토큰 확인, 토큰에 이상이 있으면 JSON으로 반환
def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")


# 다음일정 (대기)
# https://velog.io/@teddybearjung/Django-%EB%A1%9C-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EB%A7%8C%EB%93%A4%EA%B8%B010.-Login-%ED%99%94%EB%A9%B4-templates-%EB%A7%8C%EB%93%A4%EA%B8%B0-login-%ED%95%A8%EC%88%98-%EC%9E%91%EC%84%B1