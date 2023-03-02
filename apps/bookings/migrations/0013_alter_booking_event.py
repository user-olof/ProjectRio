# Generated by Django 3.2.15 on 2023-03-02 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_and_classes', '0003_delete_member'),
        ('bookings', '0012_alter_booking_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='events_and_classes.eventsandclasses'),
        ),
    ]
