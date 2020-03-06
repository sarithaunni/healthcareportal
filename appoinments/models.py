from django.db import models
from customuser.models import Customuser

# Create your models here.
class Appoinment(models.Model):
    user=models.ForeignKey(Customuser,related_name='apatient',on_delete=models.CASCADE)
    doctor=models.ForeignKey(Customuser,related_name='adoctor',on_delete=models.CASCADE)
    Gender_choices=(('Male','Male'),
        ('Female','Female'),
         )

    gender = models.CharField(max_length=10,choices=Gender_choices)
    phno = models.CharField(max_length=100)
    appoinmentdate = models.DateTimeField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode= models.IntegerField()
    state = models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
