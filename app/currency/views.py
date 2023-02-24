from django.shortcuts import render
from django.http import HttpResponse

from currency.models import Rate, ContactUs

# Create your views here.


def list_rates(request):
    qs = Rate.objects.all()
    result = []

    for rate in qs:
        result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, source: {rate.source}, created: {rate.created}<br>')

    return HttpResponse(str(result))


def list_emails(request):
    qs = ContactUs.objects.all()
    result = []

    for email in qs:
        result.append(f'id: {email.id}, from: {email.email_from}, subject: {email.subject}, message: {email.message}<br>')

    return HttpResponse(str(result))
