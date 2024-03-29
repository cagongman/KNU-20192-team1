from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user=User.objects.get(username=request.POST['userID'])
                return HttpResponse('이미 사용하고 있는 이름입니다!')
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST["userID"],password=request.POST["password1"]
                )
                user.profile.name=request.POST['name']
                user.profile.phonenumber=request.POST['phone']
                user.save()
                auth.login(request,user)
                return redirect('home')
    return render(request,'html/signup.html')

def login(request):
    if request.method =="POST":
        username=request.POST['userID']
        password=request.POST.get('password','')
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect')
    else:
        return render(request, 'html/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')