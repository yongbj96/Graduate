from django.shortcuts import render
from django.http import HttpResponse
from .models import BoardMember

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
            member.save() # 데이터베이스에 저장

        return render(request, 'register.html', res_data) # res_data를 넘겨서 html을 request

# 다음일정
# https://velog.io/@teddybearjung/Django-%EB%A1%9C-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EB%A7%8C%EB%93%A4%EA%B8%B010.-Login-%ED%99%94%EB%A9%B4-templates-%EB%A7%8C%EB%93%A4%EA%B8%B0-login-%ED%95%A8%EC%88%98-%EC%9E%91%EC%84%B1