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
    path('donate/reservation/<int:donation_id>/', views.create_donation_view, name='reservation'),
    path('create_donation/', views.create_donation_view, name='create_donation_view'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout_request', views.logout_request, name='logout'),
    path("admin-panel/", views.admin_panel, name="admin_panel"),  # HTML döndürür
    path("admin-panel/api/", views.admin_user_api, name="admin_user_api"),  # JSON API
    path('admin-panel/donors/', views.admin_donors, name='admin_donors'),
    path('admin-panel/donor-api/', views.admin_donor_api, name='admin_donor_api'),
]
