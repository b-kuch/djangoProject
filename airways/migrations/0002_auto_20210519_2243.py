# Generated by Django 3.2.3 on 2021-05-19 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airways', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField(verbose_name='Departure time')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='arrival', to='airways.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='departure', to='airways.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('production_date', models.DateField(verbose_name='Date of production')),
                ('passenger_capacity', models.IntegerField(verbose_name='Number of seats')),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.country'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Ticket price')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.flight')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.city')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.pilot'),
        ),
        migrations.AddField(
            model_name='flight',
            name='plane',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.plane'),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.city'),
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airways.city'),
        ),
    ]
