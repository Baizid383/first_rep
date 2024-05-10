from django.shortcuts import render


def reg(request):
    return render(request,'user.html')