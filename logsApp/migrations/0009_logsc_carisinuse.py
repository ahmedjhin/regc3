# Generated by Django 5.0.4 on 2024-09-13 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsApp', '0008_logsc_inusecarin'),
    ]

    operations = [
        migrations.AddField(
            model_name='logsc',
            name='carIsInUse',
            field=models.BooleanField(default=True),
        ),
    ]
