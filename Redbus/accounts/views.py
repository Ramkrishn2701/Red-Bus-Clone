from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method =='POST':

        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if username and password1 and password2 and firstname and lastname and email:
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'username is already taken')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email already taken')
                    return redirect('signup')
                else:
                    
                        user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)
                        user.save()
                        print('user created successfully')
                        return render(request,'login.html')
                    
                    
            else:
                messages.info(request,"password not matching")
                print("password not matching")
                return redirect('signup')
        else:
                        messages.info(request,'please provide all details')
                        return redirect('signup')
            
    else:
        return render(request,'signup.html') 
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'please enter valid credentials')
            return redirect('login')

         
    else:
        return render(request,'login.html') 
    
def logout(request):
    auth.logout(request)
    return redirect('/')