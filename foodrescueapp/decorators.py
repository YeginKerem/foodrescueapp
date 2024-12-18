from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def login_req(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Bu işlemi gerçekleştirmek için giriş yapmalsınız.')
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def authenticated_redirect(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Zaten giriş yaptınız.')
            return redirect("index")  
        return view_func(request, *args, **kwargs)
    return wrapper

def superuser_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Bu sayfaya erişmek için yetkiniz yok.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return wrapper