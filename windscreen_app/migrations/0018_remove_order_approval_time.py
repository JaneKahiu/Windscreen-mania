# Generated by Django 5.1.6 on 2025-03-04 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('windscreen_app', '0017_workprogress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='approval_time',
        ),
    ]
