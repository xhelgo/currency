from django.shortcuts import render

from currency.models import Rate, ContactUs

# Create your views here.


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }

    return render(request, 'rates_list.html', context)


def list_emails(request):
    emails = ContactUs.objects.all()

    context = {
        'emails': emails
    }

    return render(request, 'emails_list.html', context)
