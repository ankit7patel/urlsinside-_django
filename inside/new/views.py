from django.shortcuts import render, render,redirect
from django.http import HttpResponse
from .models import Student


# Create your views here.

# def home(request):
#     return HttpResponse("welcome to inside new page.........")


def homee(request):
    return redirect("https://www.geeksforgeeks.org/html-input-tag")

def registration(request):
    return render(request,'registration.html')

def registrationdata(request):
    # return
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    mobile=request.POST.get('mobile')
    print(name,mobile)
    Student.objects.create(Name=name,Mobile=mobile)
   
    print("data save...")
  

