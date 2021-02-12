from django.shortcuts import render
from .models import BoardMember

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #re_password = request.POST['re_password']

        member = BoardMember(
            username=username,
            password=password,
            email=email,
        )
        member.save()

        return render(request, 'register.html') # 유지? 삭제?