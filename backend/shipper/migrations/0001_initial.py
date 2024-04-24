# Generated by Django 5.0.4 on 2024-04-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shipper',
            fields=[
                ('shipper_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('pickup_address', models.CharField(max_length=200)),
                ('transfer_type', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100, null=True)),
                ('wallet_balance', models.FloatField(null=True)),
            ],
        ),
    ]
