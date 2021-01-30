from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, null=True, default='') #M, F
    age = models.IntegerField(null=True, default=0)