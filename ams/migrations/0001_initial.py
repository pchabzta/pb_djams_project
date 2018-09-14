# Generated by Django 2.1.1 on 2018-09-07 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_ref', models.CharField(max_length=6)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('close', 'CLOSE')], default='open', max_length=5)),
                ('tenant_name', models.CharField(max_length=100)),
                ('room_no', models.CharField(max_length=4)),
                ('room_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('room_acc_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('electricity_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('water_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('common_ser_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('other_ser_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('overdue_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('adjust', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('bill_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cf_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
            options={
                'ordering': ('-bill_date',),
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('cpu', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Room_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=250)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.Room_type'),
        ),
    ]
