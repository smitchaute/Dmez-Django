from django.shortcuts import render,redirect
#from ecom.models import ecom

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def account(request):
    return render(request,'account.html')

def contact(request):
    return render(request,'contact.html')

def testing(request):
    return render(request,'testing.html')