# Generated by Django 5.1.6 on 2025-03-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windscreen_app', '0020_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workprogress',
            name='vehicle_reg_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
