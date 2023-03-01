from django import forms

from currency.models import Rate, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            "buy",
            "sell",
            "source",
            "currency"
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            "name",
            "source_url"
        )
