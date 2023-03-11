from django import forms

from currency.models import Rate, Source, ContactUs


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


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs

        fields = (
            "name",
            "email_from",
            "subject",
            "message"
        )

        labels = {
            "email_from": "Email",
            "message": "Your message"
        }
