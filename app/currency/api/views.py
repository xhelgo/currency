from django.core.cache import cache
from requests import Response

from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency import constants
from currency.api.mixins import IsSuperUserMixin
from currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.choices import RateCurrencyChoices
from currency.filters import EmailsFilter, RateAPIFilter
from currency.models import Rate, Source, ContactUs


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('source')
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateAPIFilter
    ordering_fields = ('id', 'created', 'buy', 'sell')

    @action(detail=False, methods=('GET',))
    def latest(self, request, *args, **kwargs):
        latest_rates = []

        cached_rates = cache.get(constants.LATEST_RATE_CACHE)
        if cached_rates:
            return Response(cached_rates)

        for source_obj in Source.objects.all():
            for currency in RateCurrencyChoices:
                latest = Rate.objects.filter(
                    source=source_obj,
                    currency=currency) \
                    .order_by('-created') \
                    .first()

                if latest:
                    latest_rates.append(RateSerializer(instance=latest).data)

        cache.set(constants.LATEST_RATE_CACHE, latest_rates, 60 * 60 * 24 * 7)

        return Response(latest_rates)


class SourceApiView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer,)


class ContactUsViewSet(IsSuperUserMixin, viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = EmailsFilter
    ordering_fields = ('created', 'name')
    search_fields = ['name', 'email_from', 'subject']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsSuperUserMixin,)
        else:
            permission_classes = (AllowAny,)
        return [permission() for permission in permission_classes]
