from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import UserManager, BaseUserManager,AbstractBaseUser

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
        return self.username    
        

class CustomUserManager(BaseUserManager):
    email = models.EmailField(unique=True)
    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        phonenumber = extra_fields.get('phonenumber')
        name = extra_fields.get('name') 
        surname = extra_fields.get('surname')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return User.create_user(username, email=email, password=password, name=name,surname=surname,phonenumber=phonenumber,**extra_fields)

   
class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  
    is_superuser = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    customerId = models.AutoField(primary_key=True)  # Remove default value
    createdAt = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  
    is_admin = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)  # Add this line
    name = models.CharField(max_length=50, blank=True, null=True) 
    surname = models.CharField(max_length=50, blank=True, null=True) 
    USERNAME_FIELD = 'username' 
    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
        
    @classmethod
    def create_user(cls, username,is_superuser, email, password, phonenumber, name, surname,is_staff, is_active=False):
        user = cls(
            username=username,
            email=email,
            password=make_password(password),
            phonenumber=phonenumber,
            name=name,
            surname=surname,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
            
        )
        user.save()
        return user

    def check_password(self, raw_password):
        """
        Kullanıcının şifresini doğrulamak için raw_password'ü hashlenmiş şifreyle karşılaştırır.
        """
        return check_password(raw_password, self.password)
    
    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def __str__(self):
        return self.username
    

class Donation(models.Model):
    id = models.AutoField(primary_key=True)  
    item_name = models.CharField(max_length=100, default='Unknown Item')  # Add this line
    quantity = models.FloatField()  # Add this line
    expiry_date = models.DateField()
    is_reserved = models.BooleanField(default=False)  # Add this line
    reserved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserved_donations', null=True, blank=True)  # Add this line
    
    def formatted_quantity(self):
        return f"{self.quantity} kg"
      
class DonateOperations(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(null=True, blank=True)
    # Remove is_reserved and reserved_by from here
    
    @classmethod
    def create_donate(cls, item_name, quantity, expiry_date):
        if int(quantity) >= 100000:
            raise ValueError("Quantity is too high")
        donation = Donation(item_name=item_name,quantity=float(quantity)/1000, expiry_date=expiry_date)
        donation.save()
        return donation    
    @classmethod
    def get_current_donations(cls):
        return Donation.objects.all()
    
    def UserReservationSystemById():

        if(User.is_active == True):
            return True
        else:
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

class Feedback2(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone Number')
    message = models.TextField(blank=True, null=True, verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['-created_at']