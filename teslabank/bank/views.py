
from cgitb import html
from crypt import methods
from distutils.log import error
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

def index(request):
    context={}
    return render(request,'bank/index.html',context)

def pyflix(request):
    context={}
    return render(request,'bank/pyflix.html',context)
    
def login(request):

    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1,pass2)
        myuser.save()

        messages.success(request,"your account has successuly created")
        return redirect('bank/account.html')
    return render(request,'bank/login.html')

def signin(request):

    if request.method == 'POST':
        username  =request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username , password=password)


        if user is not None:   
            login(request,user)
            return render(request,'bank/index.html')

        else:
            messages.error((request,"baad redentials"))
            return redirect("base")
def loader(request):
    context={}
    return render(request, "bank/loader.html",context)

def register(request):
    context={}
    return render(request,'bank/register.html',context)

def error_404(request, exception):
        data = {}
        return render(request,'bank/404.html', data)



