from celery import shared_task
from django.conf import settings

from currency.choices import RateCurrencyChoices
from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME, OSHCHADBANK_CODE_NAME
from currency.models import Rate
from currency.utils import round_to_2_places_decimal, parse_rates, create_rate, parse_oshchad_rates


@shared_task
def send_mail(subject, message):
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    from currency.models import Source

    source, _ = Source.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank'
        }
    )

    rates = parse_rates('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        rate_data = {
            "buy": round_to_2_places_decimal(rate['buy']),
            "sell": round_to_2_places_decimal(rate['sale']),
            "currency": rate['ccy']
        }

        last_rate = Rate.objects.filter(
            currency=available_currency[rate_data['currency']],
            source=source
        ) \
            .first()

        create_rate(last_rate, rate_data, source, available_currency)


@shared_task
def parse_monobank():
    from currency.models import Source

    source, _ = Source.objects.get_or_create(
        code_name=MONOBANK_CODE_NAME,
        defaults={
            'name': 'monobank'
        }
    )

    rates = parse_rates('https://api.monobank.ua/bank/currency')

    available_currency = {
        840: RateCurrencyChoices.USD,
        978: RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['currencyCodeA'] not in available_currency:
            continue

        if rate['currencyCodeB'] == 980:
            rate_data = {
                "buy": round_to_2_places_decimal(rate['rateBuy']),
                "sell": round_to_2_places_decimal(rate['rateSell']),
                "currency": rate['currencyCodeA']
            }

            last_rate = Rate.objects.filter(
                currency=available_currency[rate_data['currency']],
                source=source
            ) \
                .first()

            create_rate(last_rate, rate_data, source, available_currency)


@shared_task
def parse_oshchad():
    from currency.models import Source

    source, _ = Source.objects.get_or_create(
        code_name=OSHCHADBANK_CODE_NAME,
        defaults={
            'name': 'oshchadbank'
        }
    )

    rates = parse_oshchad_rates()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
        'GBP': RateCurrencyChoices.GBP,
        'CAD': RateCurrencyChoices.CAD,
        'CHF': RateCurrencyChoices.CHF,
        'PLN': RateCurrencyChoices.PLN,
    }

    for rate in rates:
        if rate['Код'] not in available_currency:
            continue

        rate_data = {
            "buy": round_to_2_places_decimal(rate['Купівля']),
            "sell": round_to_2_places_decimal(rate['Продаж']),
            "currency": rate['Код']
        }

        last_rate = Rate.objects.filter(
            currency=available_currency[rate_data['currency']],
            source=source
        ) \
            .first()

        create_rate(last_rate, rate_data, source, available_currency)
