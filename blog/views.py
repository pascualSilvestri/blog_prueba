from django.shortcuts import render

def Home(request):
    return render(request,'home.html')

def Pag1(request):
    return render(request, 'pag1.html')