from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import LoginForm
from account.models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)
        return render(request, 'home.html', {'user':user})

    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#
#     elif request.method == 'POST':
#         username = request.POST.get('username',None)
#         password = request.POST.get('password',None)
#
#         res_data = {}
#         if not (username and password):
#             res_data['error'] = '모든 값을 입력해야 합니다.'
#         else:
#             user = User.objects.get(username=username)
#             if check_password(password, user.password):
#                 request.session['user'] = user.id
#                 return redirect('/')
#             else:
#                 res_data['error'] = '비밀번호가 일치하지 않습니다'
#
#         return render(request, 'login.html', res_data)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

def register(request):
    # GET 방식 요청은 데이터베이스와 관련이 없다.
    # register.html 을 응답하는 로직
    if request.method == 'GET':
        return render(request, 'register.html')

    # POST 방식 요청은 데이터베이스와 관련이 있다.
    # client 에게 요청받은 데이터를 데이터베이스에 저장하는 로직
    elif request.method == 'POST':
        # client 에게 form 을 통해서 입력받은 값을 가져온다.
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        email = request.POST.get('email',None)

        # 템플릿에 넘길 응답 데이터
        res_data={}

        # 입력받은 값이 하나라도 없는 경우
        if not (username and password and re_password and email):
            res_data['error'] = '모든값을 입력해야 합니다.'
        # 입력받은 비밀번호와 확인 비밀번호가 다른 경우
        elif password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        # 모든 값을 입력받고 비밀번호가 일치하는 경우 데이터를 받은 User 인스턴스를 생성 밑 데이터베이스에 저장
        else:
            user = User(
                username=username,
                password=make_password(password),
                email=email
            )

            user.save()
            return redirect('account:login')

        return render(request, 'register.html', res_data) # res_data = {'error':'비밀번호가 다릅니다!'}















