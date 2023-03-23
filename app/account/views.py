from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView

from account.forms import UserSignUpForm


# Create your views here.


class UserSignUpView(SuccessMessageMixin, CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')
    success_message = "Success! We have sent you the email with further instructions."
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        messages.success(self.request, 'Account activated successfully. Use your credentials to log in')
        user = get_user_model().objects.filter(username=username).first()
        if user is not None:
            user.is_active = True
            user.save()
        url = super().get_redirect_url(*args, **kwargs)
        return url
