from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView

from account.forms import UserSignUpForm, UserProfileForm


# Create your views here.


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')
    success_message = 'Your profile was updated successfully'
    queryset = get_user_model().objects.all()
    form_class = UserProfileForm
    # fields = (
    #     'first_name',
    #     'last_name',
    #     'avatar',
    #     'phone'
    # )
    # widgets = {
    #     'avatar': ClearableFileInput()
    # }

    def get_object(self, queryset=None):
        return self.request.user


class UserSignUpView(SuccessMessageMixin, CreateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super(UserSignUpView, self).dispatch(request, *args, **kwargs)

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
