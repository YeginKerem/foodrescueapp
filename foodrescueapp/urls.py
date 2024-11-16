from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayfa-1/', views.sayfa_1, name='sayfa_1'),
   
]
