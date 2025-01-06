# Generated by Django 5.1.4 on 2025-01-06 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarMake_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model_name', models.CharField(max_length=64)),
                ('CarMake_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car1.carmake')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('color', models.CharField(max_length=10)),
                ('volum', models.DecimalField(decimal_places=1, max_digits=10)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagase/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('CarMake_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car1.carmake')),
                ('car_model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car1.carmodel')),
            ],
        ),
    ]
