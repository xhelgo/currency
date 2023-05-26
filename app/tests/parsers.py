from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank, parse_monobank


def test_privatbank_parser(mocker):
    initial_count = Rate.objects.all().count()
    privat_data = [{"ccy": "EUR", "base_ccy": "UAH", "buy": "40.06640", "sale": "41.84100"},
                   {"ccy": "USD", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"}]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: privat_data
        )
    )

    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 2

    parse_privatbank()
    assert Rate.objects.all().count() == initial_count + 2

    assert request_get_mock.call_count == 2


def test_monobank_parser(mocker):
    initial_count = Rate.objects.all().count()
    mono_data = [{"currencyCodeA": 840, "currencyCodeB": 980, "date": 1682632874, "rateBuy": 38.65, "rateCross": 0,
                  "rateSell": 37.4406},
                 {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1682672774, "rateBuy": 40.22, "rateCross": 0,
                  "rateSell": 41.4508}]
    request_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(
            json=lambda: mono_data
        )
    )

    parse_monobank()
    assert Rate.objects.all().count() == initial_count + 2

    parse_monobank()
    assert Rate.objects.all().count() == initial_count + 2

    assert request_get_mock.call_count == 2
