# Generated by Django 5.1.6 on 2025-02-20 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windscreen_app', '0006_userdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='windscreen_app.vehicle'),
        ),
    ]
