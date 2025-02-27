# Generated by Django 5.1.5 on 2025-01-26 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mac_address', models.CharField(max_length=17, unique=True)),
                ('created_ad', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('energy', models.JSONField()),
                ('cos_fi_a', models.JSONField()),
                ('cos_fi_b', models.JSONField()),
                ('cos_fi_c', models.JSONField()),
                ('cos_fi_common', models.JSONField()),
                ('freq_a', models.JSONField()),
                ('freq_b', models.JSONField()),
                ('freq_c', models.JSONField()),
                ('freq_common', models.JSONField()),
                ('voltage_a', models.JSONField()),
                ('voltage_b', models.JSONField()),
                ('voltage_c', models.JSONField()),
                ('voltage_common', models.JSONField()),
                ('current_a', models.JSONField()),
                ('current_b', models.JSONField()),
                ('current_c', models.JSONField()),
                ('current_common', models.JSONField()),
                ('whole_power_a', models.JSONField()),
                ('whole_power_b', models.JSONField()),
                ('whole_power_c', models.JSONField()),
                ('active_power_a', models.JSONField()),
                ('active_power_b', models.JSONField()),
                ('active_power_c', models.JSONField()),
                ('reactive_power_a', models.JSONField()),
                ('reactive_power_b', models.JSONField()),
                ('reactive_power_c', models.JSONField()),
                ('timestamp', models.JSONField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('modem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='api.modem')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mac_address', models.CharField(max_length=17, unique=True)),
                ('vibration', models.JSONField()),
                ('temperature', models.JSONField()),
                ('created_ad', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('modem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='api.modem')),
            ],
        ),
    ]
