from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def call(request):
    return HttpResponse("welcome to inside new call page.........")