from statistics import mode
from django.db import models

# Create your models here.


class Ticket(models.Model):
    CHOICES = (
          ('high', 'high'),
          ('medium', 'medium'),
          ('low','low'),
      )
    Ticket_ID = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Priority =  models.CharField(choices=CHOICES,max_length=100, blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)