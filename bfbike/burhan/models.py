from django.db import models

# Create your models here.
class off_road(models.Model):
    date=models.DateField()
    road=models.CharField(max_length=100)
    bike=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    d_no=models.CharField(max_length=100)
    s_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    dis=models.CharField(max_length=100)
    mob1=models.CharField(max_length=100)
    mob2=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

class On_road(models.Model):
    date=models.DateField()
    road=models.CharField(max_length=100)
    bike=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    d_no=models.CharField(max_length=100)
    s_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    dis=models.CharField(max_length=100)
    mob1=models.CharField(max_length=100)
    mob2=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

