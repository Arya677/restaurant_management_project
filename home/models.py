from django.db import models

class Restaurnat(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)