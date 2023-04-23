from django.urls import path
from rest_framework.routers import DefaultRouter

from currency.api.views import RateViewSet, SourceApiView, ContactUsViewSet

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'contactus', ContactUsViewSet, basename='contactus')

urlpatterns = [
    path('sources/', SourceApiView.as_view(), name='sources')
]

urlpatterns += router.urls
