# Generated by Django 3.1.1 on 2020-11-11 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_usertable_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertable',
            name='active',
        ),
    ]
