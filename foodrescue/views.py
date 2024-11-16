from django.shortcuts import render
from .models import Donor, User

# Donor işlemleri
def donor_list(request):
    donors = Donor.objects.all()  # Donorları alıyoruz
    return render(request, 'donor_list.html', {'donors': donors})  # Template'e gönderiyoruz

def donor_detail(request, donor_id):
    donor = Donor.objects.get(id=donor_id)  # Belirli bir donor'ı alıyoruz
    return render(request, 'donor_detail.html', {'donor': donor})  # Template'e gönderiyoruz

# User işlemleri
def user_list(request):
    users = User.objects.all()  # Kullanıcıları alıyoruz
    return render(request, 'user_list.html', {'users': users})  # Template'e gönderiyoruz

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)  # Belirli bir kullanıcıyı alıyoruz
    return render(request, 'user_detail.html', {'user': user})  # Template'e gönderiyoruz
