from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=120)
    address_city = models.CharField(max_length=30)
    address_state = models.CharField(max_length=3)
    address_zip = models.PositiveIntegerField()
    birthdate = models.DateField(max_length=11)
    info = models.TextField(max_length=500)
    parents = models.CharField(max_length=200)
    teachers = models.CharField(max_length=200)
    students = models.CharField(max_length=200)
    classes = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    # Completed property is status of a task, task is either completed or not completed.

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['type']

class MessageBoard(models.Model):
    subject = models.CharField(max_length=300)
    date_added = models.TimeField(auto_now_add=True)    
    posts = models.CharField(max_length=300)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['date_added', 'subject']