from django.contrib import admin
from .models import MessageBoard
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('type', 'phone', 'address_line1', 'address_city', 'address_state', 'address_zip', 'birthdate', 'info', 'parents', 'teachers', 'students', 'classes', 'completed')

class MessageBoardAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_added', 'posts')

class CustomUserAdmin(UserAdmin):
    # Customize the fields displayed in the change list
    list_display = ['email', 'username', 'type', 'phone', 'completed']

    # Customize the fields displayed in the change form
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('type', 'phone', 'address_line1', 'address_city', 'address_state', 'address_zip', 'birthdate', 'info')}),
        ('Related info', {'fields': ('parents', 'teachers', 'students', 'school', 'classes')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Specifies the fields to be used for filtering in the admin list view
    list_filter = ['is_staff', 'type', 'is_active']


# admin.site.register(Profile, ProfileAdmin)
admin.site.register(MessageBoard, MessageBoardAdmin)
admin.site.register(User, CustomUserAdmin)