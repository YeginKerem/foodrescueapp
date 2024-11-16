from django.db import models
from django.contrib.auth.hashers import make_password

class Donor(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=128) 
    Phonenumber = models.CharField(max_length=15)
    Email = models.EmailField(unique=True)
    DonorId = models.AutoField(primary_key=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
        # Şifreyi şifrele
        if not self.Password.startswith('pbkdf2_'):
            self.Password = make_password(self.Password)
        super(Donor, self).save(*args, **kwargs)

    def __str__(self):
        return self.Username


class User(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=128)  
    Phonenumber = models.CharField(max_length=15)
    Email = models.EmailField(unique=True)
    CustomerId = models.AutoField(primary_key=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  
    is_admin = models.BooleanField(default=False) 
    name = models.CharField(max_length=50, blank=True, null=True) 
    surname = models.CharField(max_length=50, blank=True, null=True)  

    def save(self, *args, **kwargs):
        # Şifreyi şifrele
        if not self.Password.startswith('pbkdf2_'):
            self.Password = make_password(self.Password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.Username
