# Generated by Django 5.1.6 on 2025-02-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windscreen_app', '0013_alter_vehicle_year_of_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='registration_number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year_of_make',
            field=models.IntegerField(),
        ),
    ]
