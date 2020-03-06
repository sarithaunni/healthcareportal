from django.db import models

# Create your models here.
class DoctorLeave(models.Model):
    fromname=models.CharField(max_length=100)
    to=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    date=models.DateTimeField()
    reason=models.TextField(blank=True)

    def __str__(self):
        return self.fromname
