from django.db import models
from django.contrib.auth.models import AbstractUser

class Userid(AbstractUser):
    pass

class Sale(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("person", on_delete=models.CASCADE)
    
class Person(models.Model):
    user = models.OneToOneField(Userid, on_delete=models.CASCADE)

