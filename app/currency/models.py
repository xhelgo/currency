from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from currency.choices import RateCurrencyChoices


# Create your models here.


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'), message="Exchange rate can't be smaller than zero")])
    sell = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'), message="Exchange rate can't be smaller than zero")])
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', )

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
    code_name = models.CharField(max_length=64, unique=True)
    source_url = models.CharField(max_length=255)
    logo = models.FileField(
        default='sources_logos/source-default.svg',
        upload_to='sources_logos/'
    )

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request = models.CharField(max_length=16)
    time = models.FloatField()
