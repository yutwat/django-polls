from django.contrib import admin
from .models import User
from django.contrib.auth.models import AbstractUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = (
		'user_name', 
		'first_name', 
		'last_name', 
		'email', 
		'is_staff', 
		'date_joined', 
		)

	
	fieldsets = [
	(None,               {'fields': ['username', 'email']}),
	('Date information', {'fields': ['date_joined'], }),
	]
	
admin.site.register(User, UserAdmin)