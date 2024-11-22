from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('donate', views.donate, name='donate'),
    path('feedback/', views.feedback, name='feedback'),
]
