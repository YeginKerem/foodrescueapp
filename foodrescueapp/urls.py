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
    path("admin-panel/users", views.admin_panel, name="admin_panel"),  
    path("admin-panel/users-api/", views.admin_user_api, name="admin_user_api"), 
    path('admin-panel/donors/', views.admin_donors, name='admin_donors'),
    path('admin-panel/donor-api/', views.admin_donor_api, name='admin_donor_api'),
    path('admin-panel/contact/', views.admin_contact, name='admin_contact'),
    path('admin-panel/contact-api/', views.admin_contact_api, name='admin_contact_api'),
    path('contact/', views.feedback_view, name='contact'),
]