# Generated by Django 3.1.7 on 2021-03-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(choices=[('lenovo', 'LENOVO'), ('acer', 'ACER'), ('macbook', 'MACBOOK'), ('dell', 'DELL'), ('hp', 'HP'), ('asus', 'ASUS')], max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('processor', models.CharField(choices=[('core i3', 'CORE I3'), ('core i5', 'CORE I5'), ('core i7', 'CORE I7')], max_length=100)),
                ('purchased_date', models.DateField()),
                ('employee_name', models.CharField(max_length=100)),
                ('handover_date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(choices=[('lenovo', 'LENOVO'), ('samsung', 'SAMSUNG'), ('huawei', 'HUAWEI'), ('nokia', 'NOKIA')], max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('purchased_date', models.DateField()),
                ('employee_name', models.CharField(max_length=100)),
                ('handover_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(choices=[('alfa', 'ALFA'), ('mtc', 'MTC')], max_length=100)),
                ('sim_number', models.IntegerField()),
                ('line_number', models.IntegerField()),
                ('sim_type', models.CharField(choices=[('data', 'DATA'), ('primary', 'PRIMARY'), ('vpn', 'VPS')], max_length=100)),
                ('sim_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(choices=[('lenovo', 'LENOVO'), ('samsung', 'SAMSUNG'), ('huawei', 'HUAWEI')], max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('purchased_date', models.DateField()),
                ('employee_name', models.CharField(max_length=100)),
                ('handover_date', models.DateField()),
            ],
        ),
    ]
