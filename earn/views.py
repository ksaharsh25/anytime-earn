from django.shortcuts import render

# Create your views here.
def custom_user(request):
    return render(request,"custom.html")

def advisor(request):
    return render(request,"advisor.html")
    

