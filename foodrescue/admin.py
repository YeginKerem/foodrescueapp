from django.contrib import admin
from .models import Donor, User

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Phonenumber', 'is_active', 'CreatedAt') 
    list_filter = ('is_active', 'CreatedAt')  
    search_fields = ('Username', 'Email', 'Phonenumber') 
    ordering = ('-CreatedAt',)  
    readonly_fields = ('CreatedAt',)  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Phonenumber', 'is_active', 'is_admin', 'name', 'surname', 'CreatedAt')
    list_filter = ('is_active', 'is_admin', 'CreatedAt')
    search_fields = ('Username', 'Email', 'name', 'surname')
    ordering = ('-CreatedAt',)
    readonly_fields = ('CreatedAt',)
