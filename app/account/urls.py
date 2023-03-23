from django.urls import path

from account.views import (
    UserSignUpView, UserActivateView,
)

app_name = 'account'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>/', UserActivateView.as_view(), name='activate'),
]
