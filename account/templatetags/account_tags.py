from django import template
from django.shortcuts import get_object_or_404
from account.models import TenantProfile

register = template.Library()


@register.inclusion_tag('account/display_tenant_data.html')
def display_tenant_data(rmno):
    tenant_data = get_object_or_404(TenantProfile, room_no__room_no=rmno)  # str vs str !!!!

    return {'tenant_data': tenant_data}
