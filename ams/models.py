from django.db import models


class Room_type(models.Model):
    desc = models.CharField(max_length=250)
    rate = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.desc


class Room(models.Model):
    room_type = models.ForeignKey(Room_type, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=4)

    def __str__(self):
        return self.room_no


class Extra(models.Model):
    desc = models.CharField(max_length=100)
    cpu = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.desc


class Billing(models.Model):
    STATUS_CHOICE = (('open', 'OPEN'), ('close', 'CLOSE'),)

    bill_ref = models.CharField(max_length=6)
    bill_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICE, default='open')
    tenant_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=4)
    room_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    room_acc_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    electricity_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    water_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    common_ser_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    other_ser_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    overdue_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    adjust = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    bill_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    payment_date = models.DateField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cf_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    class Meta:
        ordering = ('-bill_date',)

    def __str__(self):
        return 'Bill for room number: {} Status: {}'.format(self.room_no, self.status)
