# Generated by Django 3.2.15 on 2022-12-09 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20221209_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]