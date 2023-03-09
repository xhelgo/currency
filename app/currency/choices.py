from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, 'US Dollar'
    EUR = 2, 'Euro'
    GBP = 3, 'British Pound'
    PLN = 4, 'Polish Zloty'
    CHF = 5, 'Swiss Franc'
    JPY = 6, 'Japanese Yen'
    CAD = 7, 'Canadian Dollar'
    AUD = 8, 'Australian Dollar'
