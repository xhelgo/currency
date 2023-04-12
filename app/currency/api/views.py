from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.filters import RateFilter, EmailsFilter
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
    filterset_class = RateFilter
    ordering_fields = ('id', 'created', 'buy', 'sell')


class SourceApiView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer,)


class IsSuperUser(permissions.BasePermission):
    # Check if the user is_superuser
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class ContactUsViewSet(viewsets.ModelViewSet):
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
            permission_classes = (IsSuperUser,)
        else:
            permission_classes = (AllowAny,)
        return [permission() for permission in permission_classes]
