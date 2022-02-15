from django.shortcuts import render
from basicapp.forms import UserForm,UserInfoForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def base (request):
    return render (request,'basicappo/base.html')



def home(request):
    return render(request,'basicappo/home.html')


def userlogin (request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('not active')
        else:
            return HttpResponse ('not user')
    else:
        return render (request, 'basicappo/login.html')

@login_required
def userlogout (request):
    logout (request)
    return HttpResponseRedirect (reverse ('home'))







@login_required
def special (request):
    return HttpResponse ('you r logged in')









def register(request):
    registered=False
    if request.method=='POST':
        userformobject=UserForm(data=request.POST)
        userinfoformobject=UserInfoForm(data=request.POST)
        if userformobject.is_valid() and userinfoformobject.is_valid():
            pozer=userformobject.save()
            pozer.set_password(pozer.password)
            pozer.save()
            fozer=userinfoformobject.save(commit=False)
            fozer.user=pozer
            if 'profilepic' in request.FILES:
                fozer.profilepic=request.FILES['profilepic']
            fozer.save()
            registered=True
        else:
            print(userformobject.errors,userinfoformobject.errors)
    else:
        userformobject=UserForm()
        userinfoformobject=UserInfoForm()


    dict={'registeredkey':registered ,'userformobjectkey':userformobject ,'userinfoformobjectkey':userinfoformobject}
    return render(request,'basicappo/register.html',dict)


# Create your views here.
