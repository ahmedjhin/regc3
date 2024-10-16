# Generated by Django 5.1.1 on 2024-09-08 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsApp', '0002_delete_inusecars'),
    ]

    operations = [
        migrations.CreateModel(
            name='InUseCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logsApp.registredcars')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logsApp.employesinfo')),
            ],
        ),
    ]
