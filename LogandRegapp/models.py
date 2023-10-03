from django.db import models

# Create your models here.
class Register(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    FLname=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    re_password=models.CharField(max_length=50)
    Mobile=models.IntegerField()

    def __str__(self):
        return self.FLname
