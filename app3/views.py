from django.shortcuts import render

# Create your views here.

def whatsapp(request):
    return render(request,'whatsapp.html')