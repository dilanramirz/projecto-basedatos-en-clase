# Generated by Django 4.0.4 on 2022-05-13 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.BigIntegerField()),
                ('Vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='Vehiculo',
            field=models.ManyToManyField(through='ventas.VehiculoVenta', to='vehiculos.vehiculo'),
        ),
        migrations.AddField(
            model_name='vehiculoventa',
            name='Venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta'),
        ),
    ]
