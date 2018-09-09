from django.shortcuts import render
from django.http import HttpResponse
# Create your tests here.

def homePageView(request):
    return HttpResponse('Hello, World!')