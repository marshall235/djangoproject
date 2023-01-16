# Generated by Django 4.1.5 on 2023-01-16 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_model_vehicle_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='our_customer', to='authentication.customer'),
        ),
    ]
