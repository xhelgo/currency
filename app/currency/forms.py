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

        widgets = {
            'buy': forms.TextInput(attrs={'placeholder': '38.80'}),
            'sell': forms.TextInput(attrs={'placeholder': '39.20'}),
        }

        labels = {
            "buy": "Buy rate",
            "sell": "Sell rate"
        }


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            "name",
            "source_url",
            "logo"
        )

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pryvatbank'}),
            'source_url': forms.TextInput(attrs={'placeholder': 'https://www.privatbank.ua/'}),
        }

        labels = {
            "source_url": "Source URL",
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs

        fields = (
            "name",
            "email_from",
            "subject",
            "message"
        )

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Petro Poroshenko'}),
            'email_from': forms.TextInput(attrs={'placeholder': 'example@tracky.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message...'})
        }

        labels = {
            "email_from": "Email",
            "message": "Your message"
        }
