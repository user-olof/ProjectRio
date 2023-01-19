# Generated by Django 3.2.15 on 2022-12-01 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20221129_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
