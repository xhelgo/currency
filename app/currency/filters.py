import django_filters
from django.forms import CheckboxSelectMultiple

from currency.choices import RateCurrencyChoices
from currency.models import Rate, ContactUs, Source


class MyRangeWidget(django_filters.widgets.RangeWidget):
    template_name = "widgets/my_range_widget.html"


class RateFilter(django_filters.FilterSet):
    buy = django_filters.RangeFilter(label='Buy (Min - Max):', widget=MyRangeWidget)
    sell = django_filters.RangeFilter(label='Buy (Min - Max):', widget=MyRangeWidget)
    source = django_filters.MultipleChoiceFilter(
        field_name='source',
        choices=Source.objects.values_list('id', 'name'),
        widget=CheckboxSelectMultiple
    )
    currency = django_filters.MultipleChoiceFilter(
        field_name='currency',
        choices=RateCurrencyChoices.choices,
        widget=CheckboxSelectMultiple
    )


class RateAPIFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sell': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'currency': ('exact',),
            'source': ('exact',)
        }


class EmailsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = ['name', 'subject', 'email_from']
