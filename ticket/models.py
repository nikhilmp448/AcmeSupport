# from statistics import mode
# from django.db import models

# from user.models import Account

# # Create your models here.


# class Ticket(models.Model):
#     CHOICES = (
#           ('high', 'high'),
#           ('medium', 'medium'),
#           ('low','low'),
#       )
#     user=models.ForeignKey(Account,on_delete=models.CASCADE)
#     email=models.CharField(max_length=100, blank=True,null=True)
#     Phone_Number=models.CharField(max_length=100, blank=True,null=True)
#     Ticket_ID = models.CharField(max_length=100)
#     Subject = models.CharField(max_length=100)
#     Priority =  models.CharField(choices=CHOICES,max_length=100, blank=True, null=True)
#     Created_at = models.DateTimeField(auto_now_add=True)