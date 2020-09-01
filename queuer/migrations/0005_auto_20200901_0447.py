# Generated by Django 3.1 on 2020-09-01 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queuer', '0004_auto_20200901_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='max_position',
            new_name='max_queue_number',
        ),
        migrations.AddField(
            model_name='queueentry',
            name='queue_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
