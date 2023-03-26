from django.db import models

from currency.choices import RateCurrencyChoices

# Create your models here.


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy} (id: {self.id})'


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    email_from = models.EmailField(max_length=48)
    subject = models.CharField(max_length=48)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'emails'

    def __str__(self):
        return f'From: {self.email_from}, Subject{self.subject}'


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request = models.CharField(max_length=16)
    time = models.FloatField()
