from django.shortcuts import render

def index(request):
    return render(request, 'app/Sayfa-1.html')