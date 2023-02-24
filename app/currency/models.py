from django.db import models


# Create your models here.


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=25)  # usd
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=48)
    subject = models.CharField(max_length=48)
    message = models.TextField()
