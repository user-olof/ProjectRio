# Generated by Django 3.2.15 on 2022-12-15 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_account_membership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='membership',
            new_name='member',
        ),
    ]
