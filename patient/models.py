from django.db import models
from customuser.models import Customuser
# Create your models here.
class Patient(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    Gender_choices=(('Male','Male'),
        ('Female','Female'),
         )

    gender = models.CharField(max_length=10,choices=Gender_choices)
    email = models.EmailField(unique=True)
    ph = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode= models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    blood = models.CharField(max_length=100)
    photo=models.ImageField(upload_to ='uploads/')
    is_approved=models.BooleanField(default=False)
    

    def __str__(self):
        return self.email


