from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Snipit(models.Model):
    """ snip class """

    author = models.ForeignKey(User, blank=True, null=True)
