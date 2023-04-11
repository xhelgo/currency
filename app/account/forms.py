import uuid

from django import forms
from django.contrib.auth import get_user_model
from django.urls import reverse

from settings import settings

User = get_user_model()


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Enter password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Re-enter password')

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2'
        )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords should match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        user.is_active = False
        user.username = uuid.uuid4()
        user.set_password(password)
        user.save()

        self._send_mail()

        return user

    def _send_mail(self):
        subject = 'Thanks for signing up!'
        path = reverse('account:activate', args=(self.instance.username,))
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
        {settings.HTTP_SCHEMA}://{settings.HOST}{path}
                '''

        from django.core.mail import send_mail
        send_mail(
            subject,
            message,
            recipient,
            [self.instance.email],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'data-mask': "(000) 00-000-0000", 'placeholder': "(380) 97-977-9977"}),
        label='Phone number',
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'avatar',
            'phone'
        )
