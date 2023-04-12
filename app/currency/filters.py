import django_filters

from currency.models import Rate, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate

        fields = ['buy', 'sell', 'currency', 'source']

        # affects the form rendering
        # fields = {
        #     'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
        #     'sell': ('gt', 'gte', 'lt', 'lte', 'exact'),
        #     'currency': "",
        #     'source': ""
        # }


class EmailsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = ['name', 'subject', 'email_from']
