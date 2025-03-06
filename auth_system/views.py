from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        un=request.POST.get('un')
        em=request.POST.get('em')
        pw1=request.POST.get('pw1')
        pw2=request.POST.get('pw2')
        if pw1==pw2:
            if not User.objects.filter(username=un).exists():
                User.objects.create_user(username=un,email=em,password=pw1)
                return redirect('login')
            else:
                return render(request,'signup.html',{'msg':'username already exists'})
        
        else:
            return render(request,'signup.html',{'msg':'password is not matching'})

    return render(request,'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        user= authenticate(request,username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            return render(request,'login.html',{'msg':'invalid username or password'})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

            
   
        
