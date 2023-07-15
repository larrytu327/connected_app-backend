from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class MessageBoard(models.Model):
    subject = models.CharField(max_length=300)
    date_added = models.TimeField(auto_now_add=True)    
    posts = models.CharField(max_length=300)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['date_added', 'subject']

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user
    
class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address_line1 = models.CharField(verbose_name='address line 1', max_length=120)
    address_city = models.CharField(max_length=30)
    address_state = models.CharField(max_length=3)
    address_zip = models.PositiveIntegerField(null=True, blank=True)
    birthdate = models.DateField(max_length=11, null=True, blank=True)
    info = models.TextField(max_length=500)
    parents = models.CharField(max_length=200)
    teachers = models.CharField(max_length=200)
    students = models.CharField(max_length=200)
    school = models.CharField(max_length=50)
    classes = models.CharField(max_length=200)
    # Completed property is status of a task, task is either completed or not completed.
    completed = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, null=True, blank=True)
    # last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
    
    def __str__(self):
        return self.username
    
    class Meta: 
        ordering = ['type', 'email']