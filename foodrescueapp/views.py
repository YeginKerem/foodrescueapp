from django.shortcuts import render

def sayfa_1(request):
    return render(request, 'app/Sayfa-1.html')