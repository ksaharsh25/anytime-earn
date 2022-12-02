from django.shortcuts import render,redirect
from .models import *
import random
# Create your views here.
def register(request):
    if request.method=="POST":
        try:
            
            first_name=request.POST['name']
            last_name=request.POST['last_name']
            mobile=request.POST['mobile']
            
            admin=CustomUser(first_name=first_name,last_name=last_name,mobile=mobile)
            
            admin.save()
            
        except admin.DoesNotExist:
            print("Error!")
        return redirect('login')    
        
    return render(request, 'register.html')

def get_otp():
    otp=""
    for i in  range(5):
        otp+=str(random.randint(1,9))
    return otp   

def login(request):
    if request.method=="POST":
        mobile=request.POST.get('mobile')
        
        try:
            mob=CustomUser.objects.get(mobile=mobile)
            
        except:
            CustomUser.objects.create(mobile=mobile)
            mob=CustomUser.objects.get(mobile=mobile)
            
        request.session['mobile']=mobile
        OTP=get_otp()
        mob.otp=OTP
        mob.save()
        
        return redirect('verify')    
    return render(request,'login.html')  



def custom_user(request):
    return render(request,"custom.html")

def advisor(request):
    return render(request,"advisor.html")
    

