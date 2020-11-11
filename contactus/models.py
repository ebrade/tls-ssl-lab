from django.db import models


# Create your models here.

class ContactUS(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Contact Us'
