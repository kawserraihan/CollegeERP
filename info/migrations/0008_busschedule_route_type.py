# Generated by Django 4.2.5 on 2023-12-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_busschedule_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='busschedule',
            name='route_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
