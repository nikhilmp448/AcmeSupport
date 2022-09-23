from statistics import mode
from django.db import models

# Create your models here.


class Ticket(models.Model):
    Ticket_ID = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Priority = models.CharField(max_length=100)
    Created_at = models.DateTimeField(auto_now_add=True)