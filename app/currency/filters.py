import django_filters

from currency.models import Rate, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = ['buy', 'sell', 'currency', 'source']


class EmailsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = ['name', 'subject', 'email_from']
