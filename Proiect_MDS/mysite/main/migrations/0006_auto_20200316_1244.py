# Generated by Django 3.0.3 on 2020-03-16 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200316_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='materials_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 44, 15, 462340), verbose_name='date published'),
        ),
    ]
