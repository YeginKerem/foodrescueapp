from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('donate', views.create_donation_view, name='donate'),
    path('feedback/', views.feedback, name='feedback'),
    path('donate/delete/<int:donation_id>/', views.delete_donation_view, name='delete_donation'),
    path('reserve_donation/<int:donation_id>/', views.reserve_donation_view, name='reserve_donation'),
    path('cancel_reservation/<int:donation_id>/', views.cancel_reservation_view, name='cancel_reservation'),
    path('create_donation/', views.create_donation_view, name='create_donation_view'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout_request', views.logout_request, name='logout'),

]
