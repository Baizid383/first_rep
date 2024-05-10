from django.shortcuts import render,HttpResponse

# Create your views here.


def index(Request):
    return HttpResponse('this is division')