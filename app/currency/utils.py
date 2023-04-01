from decimal import Decimal

from bs4 import BeautifulSoup
import requests

from currency.models import Rate


def round_to_2_places_decimal(value: str) -> Decimal:
    """
    Convert a value to Decimal with two decimal places
        example:
        '123.123' -> Decimal(123.12)
    """
    return round(Decimal(value), 2)


def parse_rates(url: str) -> list:
    """Returns a list of dictionaries with rates' details"""
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    return rates


def get_last_rate(currency_code, source, available_currency):
    last_rate = Rate.objects.filter(
        currency=available_currency[currency_code],
        source=source
    ) \
        .first()

    return last_rate


def create_rate(rate_data, source, available_currency):
    last_rate = get_last_rate(rate_data["currency"], source, available_currency)
    if last_rate is None or last_rate.buy != rate_data["buy"] or last_rate.sell != rate_data["sell"]:
        Rate.objects.create(
            buy=rate_data["buy"],
            sell=rate_data["sell"],
            currency=available_currency[rate_data["currency"]],
            source=source
        )


def parse_oshchad_rates(url: str = 'https://www.oschadbank.ua/currency-rate') -> list[dict]:
    """
    Parse a list of dictionaries with rates' details from oschadbank site
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    rates = soup.find_all('tr', class_='heading-block-currency-rate__table-row')

    # returns table header from oschadbank: ['Валюта', 'Код', 'Кількість одиниць', 'Купівля', 'Продаж', 'Курс НБУ']
    keys = [td.text for td in rates[0].find_all('td')]

    # creates a dict (in this format {'Валюта': 'Долар США', 'Код': 'USD', ... } for every rate in the selected range
    rates_dict = [{k: td.text for k, td in zip(keys, rate.find_all('td'))} for rate in rates[1:8]]

    return rates_dict
