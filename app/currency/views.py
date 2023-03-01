from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect

from currency.models import Rate, ContactUs, Source

from currency.forms import RateForm, SourceForm

# Create your views here.


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }

    return render(request, 'rates_list.html', context)


def rate_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'rate': rate
    }

    return render(request, 'rate_details.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rates/list/')
    elif request.method == 'GET':
        form = RateForm

    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rates/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form,
        'rate': rate
    }
    return render(request, 'rate_update.html', context)


def rate_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rates/list/')
    elif request.method == 'GET':
        context = {
            'rate': rate
        }
        return render(request, 'rate_delete.html', context)


def list_emails(request):
    emails = ContactUs.objects.all()

    context = {
        'emails': emails
    }

    return render(request, 'emails_list.html', context)


def list_sources(request):
    sources = Source.objects.all()

    context = {
        'sources': sources
    }

    return render(request, 'sources_list.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)

    context = {
        'source': source
    }

    return render(request, 'source_details.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sources/list/')
    elif request.method == 'GET':
        form = SourceForm

    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sources/list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form,
        'source': source
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/sources/list/')
    elif request.method == 'GET':
        context = {
            'source': source
        }
        return render(request, 'source_delete.html', context)
