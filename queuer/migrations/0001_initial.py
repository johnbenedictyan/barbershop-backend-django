# Generated by Django 3.1 on 2020-08-31 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waiting_time', models.PositiveIntegerField(default=0)),
                ('barber', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='queue', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Queue',
                'verbose_name_plural': 'Queues',
            },
        ),
        migrations.CreateModel(
            name='QueueEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.UUID('d2bc9c65-d524-459b-9caf-78a3ad2d2cf6'), max_length=36)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('valid', models.BooleanField(default=True)),
                ('queue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queuer.queue')),
            ],
            options={
                'verbose_name': 'Queue Entry',
                'verbose_name_plural': 'Queue Entries',
            },
        ),
    ]
