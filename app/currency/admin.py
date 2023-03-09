from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from currency.models import Rate, Source, ContactUs

# Register your models here.


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'currency',
        'buy',
        'sell',
        'source',
        'created',
    )
    list_filter = (
        'currency',
        'source',
        ('created', DateRangeFilter),
    )

    def get_rangefilter_created_title(self, request, field_path):
        """Change date range filter title"""
        return 'By date:'

    search_fields = (
        'source',
    )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
    )
    search_fields = (
        'name',
    )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'short_message',
    )

    search_fields = (
        'email_from',
        'subject',
        'message',
    )

    @admin.display(description="message")
    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
