from django.db import models
from customuser.models import Customuser

# Create your models here.
#name,gender,email,phno,birthdate,specilized_in,hospitalname,hospitaladdress,hospitalstate,hospitaldistrict,shift,address,city,state,pincode,country,photo,username,password
class Doctor(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    Gender_choices=(('Male','Male'),
        ('Female','Female'),
         )
    Shift_choices=(('Morning(7am-1pm)','Morning(7am-1pm)'),
        ('Afternoon(1pm to 7pm)','Afternoon(1pm to 7pm)'),
         )
    gender = models.CharField(max_length=10,choices=Gender_choices)
    email = models.EmailField(unique=True)
    ph = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    specilized_in = models.CharField(max_length=100)
    hospitalname = models.CharField(max_length=100)
    hospitaladdress = models.CharField(max_length=100)
    hospitalstate = models.CharField(max_length=100)
    hospitaldistrict = models.CharField(max_length=100)
    shift = models.CharField(max_length=100,choices=Shift_choices)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode= models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo=models.ImageField(upload_to ='uploads/')
    is_approved=models.BooleanField(default=False)
    

    def __str__(self):
        return self.email









