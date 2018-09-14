from django.urls import path
from . import views

urlpatterns = [
    path('', views.gateway, name='gateway'),
    path('create_contract/', views.create_contract, name='create_contract'),
    path('edit_contract/', views.edit_contract, name='edit_contract'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('billing/', views.billing, name='billing'),

]
