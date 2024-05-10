from django.db import models


    

class Users(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    pw = models.CharField(max_length=500)
    Phone_number= models.CharField(max_length=500)
    v_code = models.CharField(max_length=500,unique=True)
    v_statas= models.CharField(max_length=500)
