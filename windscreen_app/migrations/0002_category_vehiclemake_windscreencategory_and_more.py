# Generated by Django 5.1.5 on 2025-02-04 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windscreen_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WindscreenCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='windscreen',
        ),
        migrations.RemoveField(
            model_name='windscreen',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='windscreen',
            name='price',
        ),
        migrations.AlterField(
            model_name='windscreen',
            name='make',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='windscreen',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='windscreen',
            name='type',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='InsuranceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coverage_type', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='windscreen_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='windscreen_app.vehiclemake')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=15, unique=True)),
                ('year_of_make', models.IntegerField()),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='windscreen_app.vehiclemake')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='windscreen_app.vehiclemodel')),
            ],
        ),
        migrations.AlterField(
            model_name='windscreen',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='windscreens', to='windscreen_app.windscreencategory'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
