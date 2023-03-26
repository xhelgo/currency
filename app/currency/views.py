from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from settings import settings
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm


# Create your views here.


class RateListView(ListView):
    template_name = 'rates_list.html'

    def get_queryset(self):
        return Rate.objects.all().select_related('source')


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class RateCreateView(SuccessMessageMixin, CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rates-list')
    success_message = 'Rate was created successfully'


class RateUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rates-list')
    success_message = 'Rate was updated successfully'
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rates-list')
    success_message = 'Rate was deleted successfully'

    def test_func(self):
        return self.request.user.is_superuser


class EmailListView(ListView):
    template_name = 'emails_list.html'

    def get_queryset(self):
        return ContactUs.objects.all()


class ContactUsCreateView(SuccessMessageMixin, CreateView):
    form_class = ContactUsForm
    template_name = 'contact_us_create.html'
    success_url = reverse_lazy('currency:contact-us-create')
    success_message = 'Your message was sent successfully'

    def _send_mail(self):
        subject = 'User ContactUs'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
                    Request from: {self.object.name}.
                    Reply to email: {self.object.email_from}.
                    Subject: {self.object.subject}.
                    Body: {self.object.message}.
                '''

        from django.core.mail import send_mail
        send_mail(
            subject,
            message,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class SourceListView(ListView):
    template_name = 'sources_list.html'

    def get_queryset(self):
        return Source.objects.all()


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceCreateView(SuccessMessageMixin, CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:sources-list')
    success_message = 'Source was created successfully'


class SourceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:sources-list')
    success_message = 'Source was updated successfully'
    queryset = Source.objects.all()


class SourceDeleteView(SuccessMessageMixin, DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:sources-list')
    success_message = 'Source was deleted successfully'


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('currency:profile')
    success_message = 'Your profile was updated successfully'
    queryset = get_user_model().objects.all()
    fields = (
        'first_name',
        'last_name'
    )

    def get_object(self, queryset=None):
        return self.request.user
