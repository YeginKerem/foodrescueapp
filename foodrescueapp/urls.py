from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('donate', views.create_donation_view, name='donate'),
    path('feedback/', views.feedback, name='feedback'),
    path('donate/delete/<int:donation_id>/', views.delete_donation_view, name='delete_donation'),
    path('create_donation/', views.create_donation_view, name='create_donation_view'),
]
