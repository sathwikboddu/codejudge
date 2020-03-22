from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    email = models.CharField(max_length=200)
    location_type = models.CharField(max_length=200)
    location_string = models.CharField(max_length=200)

    def __str__(self):
        return '{} {} {} {} {} {} '.format(self.first_name, self.last_name, self.mobile,self.email,self.location_type,self.location_string)