from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Cart(models.Model):
    card_id = models.CharField(max_length=250)