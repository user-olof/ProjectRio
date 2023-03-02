# Generated by Django 3.2.15 on 2023-03-01 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_account_user'),
        ('bookings', '0010_remove_booking_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='account',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
    ]
