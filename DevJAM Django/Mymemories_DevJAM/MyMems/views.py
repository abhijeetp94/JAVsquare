from django.shortcuts import render
from django.http import HttpResponse
from .models import user_details,note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import forms

# Create your views here.
def index(request):
    
    return render(request,'MyMems/index.html')

def productivity(request):
    return render(request,'MyMems/login.html')

def images(request):
    return render(request,'MyMems/login.html')

def dairy(request):
    global user_name
    user_name = request.POST.get('uname', "")
    pass_word = request.POST.get('pass', "")
    auth = User.objects.values('username', 'password')
    print(auth)
    if not any(d['username'] == user_name and d['password'] == pass_word for d in auth):
    # global vali
    # vali = authenticate(request,username= user_name, password= pass_word)
    # print(vali)
    # # login(request,vali)

    # rq = {'vali': vali}

    # if vali is not None:
        
    #     login(request)
        return render(request,'MyMems/dairy.html')        
    else:
        # print(vali)
        return render(request, 'MyMems/loginerror.html')

def mistakes(request):
    return render(request,'MyMems/index.html')

def goals(request):
    return render(request,'MyMems/index.html')

def login(request):
    return render(request, 'MyMems/login.html')

def signup(request):

    
    return render(request,'MyMems/signup.html')

def signupsuccess(request):
    finame = request.POST.get('fname', '')
    laname = request.POST.get('lname', '')
    usnm = request.POST.get('usn', '')
    psw = request.POST.get('passw', '')
    repsw = request.POST.get('re_pass', '')
    aterm = request.POST.get('term', 'uncheck')

    


    if psw != repsw:
        return render(request, 'MyMems/passworderror.html')
    
    elif len(usnm)<=0  or len(psw)<=0 or len(finame)<=0 or len(laname)<=0:
        return request(request,'MyMems/empty_value.html')

    elif aterm == 'uncheck':
        return request(request,'MyMems/checkbox.html')
    
    else:
        us = User.objects.create_user(usnm,'',psw)
        us.first_name = finame
        us.last_name = laname
        us.save()
        return render(request,'MyMems/loginsuccess.html')


def upload(request):
        user = user_name
        msg = request.POST.get('message', '')
        title = request.POST.get('titlename', '')
        # unm = request.POST.get('un', '')
        # print(vali)


        if len(msg)>0 and len(title)>0:
            addmsg = note(uname = user, notesname = title, notes = msg)
            addmsg.save()
            return render(request, 'MyMems/uploaded.html')

        else:
            return render(request, 'MyMems/notuploaded.html')