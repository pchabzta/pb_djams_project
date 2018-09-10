from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
from ams.models import Room, Extra, Room_type

from django.urls import reverse


class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(default=0)
    pass  # Per default setting, No added fields required

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
        # return self.first_name


class TenantProfile(models.Model):
    tenant = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    pin = models.CharField(max_length=13, unique=True)
    phone = models.CharField(max_length=10)
    room_no = models.OneToOneField(Room, on_delete=models.CASCADE, unique=True)
    term = models.PositiveSmallIntegerField(default=12)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    deposit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    deduct = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cum_ovd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0)
    adjust = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    extra = models.ManyToManyField(Extra)

    bill_date = models.DateField(auto_now=True, blank=True)
    elec_unit = models.IntegerField(blank=True, null=True)  # use placeholder
    water_unit = models.IntegerField(blank=True, null=True)
    misc_cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.tenant.first_name)

    def get_absolute_url(self):
        return reverse('fill_bill', args=[self.room_no])
