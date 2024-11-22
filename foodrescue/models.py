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
    id = models.AutoField(primary_key=True)  # Ensure there is a primary key field with a default value
    item_name = models.CharField(max_length=100, default='Unknown Item')  # Add a default value for item_name
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    @classmethod
    def create_donate(cls, item, quantity, expiry_date):
        donation = cls(item_name=item, quantity=quantity, expiry_date=expiry_date)
        donation.save()
        return donation

    @classmethod
    def get_current_donations(cls):
        return cls.objects.all()
   
        
class DonateOperations(models.Model):

    @staticmethod
    def create_donate(item, quantity, expiry_date):
        donation = Donation(item_name=item, quantity=quantity, expiry_date=expiry_date)
        donation.save()
        return donation

    @staticmethod
    def get_current_donations():
        return Donation.objects.all()

    @staticmethod
    def delete_donation_by_id(item_id):
        try:
            donation = Donation.objects.get(ItemId=item_id)
            donation.delete()
            return True
        except Donation.DoesNotExist:
            return False

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedbackText = models.TextField(null=False, blank=False)  
    feedbackDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Feedback from {self.user.username} at {self.feedbackDate}"
   
    @staticmethod
    def create_feedback(user, feedbackText):
        feedback = Feedback(
            user=user,
            feedbackText=feedbackText
        )
        feedback.save()
        return None

    @staticmethod
    def update_feedback(user, feedbackText):
        try:
            feedback = Feedback.objects.get(user=user)
            feedback.feedbackText = feedbackText
            feedback.save()
            return feedback
        except Feedback.DoesNotExist:
            return True

    @staticmethod
    def delete_feedback(user):
        try:
            feedback = Feedback.objects.get(user=user)
            feedback.delete()
            return True
        except Feedback.DoesNotExist:
            return False