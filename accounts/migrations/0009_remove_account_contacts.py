# Generated by Django 2.2.3 on 2019-07-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='contacts',
        ),
    ]
