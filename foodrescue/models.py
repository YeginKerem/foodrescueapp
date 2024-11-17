from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import UserManager

class Donor(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128) 
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    donorId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
       
        self.Password = make_password(self.Password)
        super(Donor, self).save(*args, **kwargs)

    def __str__(self):
        return self.Username
        


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  
    phonenumber = models.CharField(max_length=15,)
    email = models.EmailField(unique=True)
    customerId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  
    is_admin = models.BooleanField(default=False) 
    name = models.CharField(max_length=50, blank=True, null=True) 
    surname = models.CharField(max_length=50, blank=True, null=True)  

    @classmethod
    def create_user(cls, username, email, password, phonenumber, name, surname, is_active=False):
        user = cls(
            username=username,
            email=email,
            password=make_password(password),
            phonenumber=phonenumber,
            name=name,
            surname=surname,
            is_active=is_active,
        )
        user.save()
        return user

    def check_password(self, raw_password):
        """
        Kullanıcının şifresini doğrulamak için raw_password'ü hashlenmiş şifreyle karşılaştırır.
        """
        return check_password(raw_password, self.password)
    
    


    def __str__(self):
        return self.username
    

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    ItemId = models.AutoField(primary_key=True)
    donationDate = models.DateTimeField(auto_now_add=True)
    expiryDate = models.DateField() 
    quantity = models.PositiveIntegerField() 

    def str(self):
        return f"{self.donor.username} - {self.item_id}"
