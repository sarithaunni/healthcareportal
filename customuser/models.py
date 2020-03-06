from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self,email,type,username,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            type=type,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, type,username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            type,
            username,
            password,
            
        )
        user.is_admin = True
        user.is_staff=True
        user.save(using=self._db)
        return user

class Customuser(AbstractBaseUser):
   
    
    Type_choices=(('Doctor','Doctor'),
        ('Patient','Patient'),
        ('Admin','Admin'),
         )
    email = models.EmailField(unique=True)
    
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=Type_choices)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','type'
    ]

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True








