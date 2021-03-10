from django.shortcuts import render, redirect
from member.models import BoardMember

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username    = request.POST.get('username', None)
        password    = request.POST['password']

        member = BoardMember(
                username = username,
                password = password,
            )

        print("#####로그인#####\nid: ", member.username, "\npw: ", member.password, "\nemail: ", member.email)

        return redirect('api/token/', member) # api/token에 GET method로 호출;;