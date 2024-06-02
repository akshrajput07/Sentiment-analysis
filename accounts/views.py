from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re
# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'pages/login.html')



def register(request):
    if request.method =='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name'] 
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password2']
        #print(password1, password2)
        if contains_number(first_name) or contains_number(last_name):
            messages.info(request,'**Enter valid names')
            return redirect('register')
            
        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'**Username already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'**Email already Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password2,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
        else:
            messages.info(request,'**Password not matching ')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,'pages/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def contains_number(string):
    return bool(re.search(r'\d', string))