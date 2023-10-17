from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Calculateexpense(models.Model):
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    Total_participants = models.IntegerField(null=True,blank=True)

class Participantowe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='all_users',null=True,blank=True)
    first_installment = models.IntegerField(null=True,blank=True)
    second_installment = models.IntegerField(null=True,blank=True)
    third_installment = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    first_installment_receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='first_installment_receivers',null=True,blank=True)
    second_installment_receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='second_installment_receivers',null=True,blank=True)
    third_installment_receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='third_installment_receivers',null=True,blank=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='users_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)