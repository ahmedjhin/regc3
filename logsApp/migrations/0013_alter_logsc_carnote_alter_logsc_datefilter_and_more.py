# Generated by Django 5.0.4 on 2024-09-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsApp', '0012_logsc_datefilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logsc',
            name='carNote',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='logsc',
            name='dateFilter',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registredcars',
            name='carNumber',
            field=models.TextField(default=0),
        ),
    ]
