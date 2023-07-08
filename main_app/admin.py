from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('type', 'username', 'email', 'phone', 'address_line1', 'address_city', 'address_state', 'address_zip', 'birthdate', 'info', 'parents', 'teachers', 'students', 'classes', 'completed')

admin.site.register(User, UserAdmin)