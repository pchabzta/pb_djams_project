from django.urls import path
from . import views

urlpatterns = [

    path('monthly_report/', views.monthly_report, name='monthly_report'),
    path('payment/', views.payment, name='payment'),
    path('tenant_record/', views.tenant_record, name='tenant_record'),
    path('tenant_comment/', views.tenant_comment, name='tenant_comment'),
    path('report_parameters/', views.report_parameters, name='report_parameters'),
    path('report_type/', views.report_type, name='report_type'),
    path('extra_service/', views.extra_service, name='extra_service'),
    path('elec_cpu_change/', views.elec_cpu_change, name='elec_cpu_change'),
    path('water_cpu_change/', views.water_cpu_change, name='water_cpu_change'),
    path('room_type_rate/', views.room_type_rate, name='room_type_rate'),
    path('current_tenant/', views.current_tenant, name='current_tenant'),
    path('vacant_rooms/', views.vacant_rooms, name='vacant_rooms'),
    path('misc_contents/', views.misc_contents, name='misc_contents'),
    path('send_sms_to_individual_room/', views.send_sms_to_individual_room, name='send_sms_to_individual_room'),
    path('send_general_sms/', views.send_general_sms, name='send_general_sms'),
    path('send_bill_sms_to_all_tenants/', views.send_bill_sms_to_all_tenants, name='send_bil_sms_to_all_tenants'),
    path('tenant_page/', views.tenant_page, name='tenant_page'),
    path('tenant_bill/', views.tenant_bill, name='tenant_bill'),
    path('new_tenant/',views.new_tenant, name='new_tenant'),

]
