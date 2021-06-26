from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def hardware(request):
    return render(request,'core/Hardware.html')