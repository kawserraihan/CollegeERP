from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


User = get_user_model

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=True, max_length=255)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null = True)
    address = models.TextField(blank=True)
    contact_number = models.CharField(blank=True, max_length=15)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_groups',  # Updated related_name for groups
        related_query_name='customuser',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_permissions',  # Updated related_name for user_permissions
        related_query_name='customuser',
        verbose_name='user permissions'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Day(models.Model):
    
    day= models.CharField(max_length=10)

    def __str__(self):
        return self.day

class BusSchedule(models.Model):
    time = models.CharField(max_length=10)
    bus_no = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length=20, null = True, blank = True)
    bus_type = models.CharField(max_length=20, null=True, blank=True)
    route_type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.day.day} - {self.time} - Bus {self.bus_no}"
    




    



