from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
