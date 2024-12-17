from django.contrib import admin
from .models import Donor, User, Donation, Feedback2

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phonenumber', 'is_active', 'createdAt') 
    list_filter = ('is_active', 'createdAt')  
    search_fields = ('username', 'email', 'phonenumber') 
    ordering = ('-createdAt',)  
    readonly_fields = ('createdAt',)  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phonenumber', 'is_active', 'is_admin', 'name', 'surname', 'createdAt')
    list_filter = ('is_active', 'is_admin', 'createdAt')
    search_fields = ('username', 'email', 'name', 'surname')
    ordering = ('-createdAt',)
    readonly_fields = ('createdAt',)
    
class DonationsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'expiry_date')
    list_filter = ('expiry_date',)
    ordering = ('expiry_date',)

@admin.register(Feedback2)
class Feedback2Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone_number', 'message')

admin.site.register(Donation, DonationsAdmin)