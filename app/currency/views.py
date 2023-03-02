from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm


# Create your views here.


class RateListView(ListView):
    template_name = 'rates_list.html'

    def get_queryset(self):
        return Rate.objects.all()


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rates-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rates-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rates-list')


class EmailListView(ListView):
    template_name = 'emails_list.html'

    def get_queryset(self):
        return ContactUs.objects.all()


class SourceListView(ListView):
    template_name = 'sources_list.html'

    def get_queryset(self):
        return Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:sources-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:sources-list')
    queryset = Source.objects.all()


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:sources-list')


class IndexView(TemplateView):
    template_name = 'index.html'
