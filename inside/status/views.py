from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def stat(request):
    return HttpResponse("welcome to inside new status page.........")