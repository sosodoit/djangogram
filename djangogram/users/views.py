from django.http.response import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html') # 호출되는 템플릿을 작성해야함
        # 페이지를 보기위한 GET 방식 요청은 이 위치에서 처리

    elif request.method == 'POST':
        # 로그인 요청에 따른 POST 방식은 이 위치에서 처리
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('posts:index'))
        
        else:
        # Return an 'invalid login' error message.
            return render(request, 'users/main.html')
