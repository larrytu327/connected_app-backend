from django.db import models

# Create your models here.
class User(models.Model):
    type = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120, default='First Name')
    last_name = models.CharField(max_length=120, default='Last Name')
    email = models.EmailField(max_length=120)
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
        return self.username