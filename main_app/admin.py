from django.contrib import admin
from .models import Profile, MessageBoard
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('type', 'phone', 'address_line1', 'address_city', 'address_state', 'address_zip', 'birthdate', 'info', 'parents', 'teachers', 'students', 'classes', 'completed')

class MessageBoardAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_added', 'posts')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(MessageBoard, MessageBoardAdmin)