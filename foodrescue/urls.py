from django.urls import path
from . import views


urlpatterns = [
    # # Donor işlemleri
    # path('donors/', views.donor_list, name='donor_list'),  # Donorların listesini gösterecek
    # path('donor/<int:donor_id>/', views.donor_detail, name='donor_detail'),  # Her donorın detaylarını gösterecek

    # # User işlemleri
    # path('users/', views.user_list, name='user_list'),  # Kullanıcıların listesini gösterecek
    # path('user/<int:user_id>/', views.user_detail, name='user_detail'),  # Her kullanıcının detaylarını gösterecek
]