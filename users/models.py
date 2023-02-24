from django.db import models
from core.models import *

class activitie(models.Model):
    email = models.OneToOneField(account, null=True, on_delete=models.CASCADE)
    was_logedin = models.BooleanField(default = False)
    was_logedout = models.BooleanField(default = False)
    def __int__(self):
         return self.email
