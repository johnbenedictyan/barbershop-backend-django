# Generated by Django 3.1 on 2020-09-01 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queuer', '0005_auto_20200901_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='max_queue_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
