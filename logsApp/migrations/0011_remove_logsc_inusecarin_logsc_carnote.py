# Generated by Django 5.1.1 on 2024-09-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsApp', '0010_employesinfo_emphavecar_registredcars_carisinparking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logsc',
            name='inusecarin',
        ),
        migrations.AddField(
            model_name='logsc',
            name='carNote',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
