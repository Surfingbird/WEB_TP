# Generated by Django 2.1.2 on 2018-10-27 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20181027_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_creation',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 27, 11, 47, 9, 35339)),
        ),
    ]
