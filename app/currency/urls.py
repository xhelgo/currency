from django.urls import path

from currency.views import (
    RateListView,
    RateCreateView,
    RateDetailView,
    RateUpdateView,
    RateDeleteView,
    EmailListView,
    SourceListView,
    SourceCreateView,
    SourceDetailView,
    SourceUpdateView,
    SourceDeleteView
)

app_name = 'currency'

urlpatterns = [
    path('sources/list/', SourceListView.as_view(), name='sources-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),

    path('emails/list/', EmailListView.as_view(), name='emails-list'),

    path('rates/list/', RateListView.as_view(), name='rates-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details')
]
