# Generated by Django 3.1.1 on 2020-11-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_remove_usertable_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
