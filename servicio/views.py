from django.shortcuts import render

# Create your views here.

def servicio(request):
    return render(request,"servicio.html")