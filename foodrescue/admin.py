from django.contrib import admin
from .models import Donor, User, Donation

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
    
@admin.register(Donation)
class DonationsAdmin(admin.ModelAdmin):
    list_display = ('ItemId', 'donor', 'expiryDate', 'donationDate', 'quantity')  
    list_filter = ('expiryDate', 'ItemId') 
    search_fields = ('ItemId',)  
    ordering = ('-donationDate',)  