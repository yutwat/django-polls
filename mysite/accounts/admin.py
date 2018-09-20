from django.contrib import admin
from .models import User
from django.contrib.auth.models import AbstractUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = (
		'username', 
		'first_name', 
		'last_name', 
		'email', 
		'is_staff',
		'is_superuser',  
		'date_joined', 
		)

	
	fieldsets = [
		(None, {
			'fields': ['username', 'email', ],
		}),
		('Advanced options', {
			'classes': ('collapse',),
			'fields': ['first_name', 'last_name', 'is_staff','is_superuser', ], 
		}),
		('Date information', {
			'fields': ['date_joined', ],
		}),
	]
	list_filter = ['username', 'email', 'is_staff', 'is_superuser', 'date_joined',]
	search_fields = ['username', 'email']
	
admin.site.register(User, UserAdmin)