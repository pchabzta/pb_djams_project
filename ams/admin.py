from django.contrib import admin
from .models import Room_type, Room, Extra, Billing

admin.site.register(Room)
admin.site.register(Room_type)
admin.site.register(Extra)


# admin.site.register(Billing)

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = (
        'bill_ref', 'room_no', 'tenant_name', 'bill_date', 'overdue_amount', 'bill_total', 'payment_amount',
        'cf_amount',
        'status')
    list_filter = ('bill_ref', 'tenant_name', 'bill_date', 'status')
    search_fields = ('tenant_name', 'bill_ref')
