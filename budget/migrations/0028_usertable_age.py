# Generated by Django 3.1.1 on 2021-01-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0027_remove_usertable_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
