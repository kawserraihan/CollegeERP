# Generated by Django 4.2.5 on 2023-10-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
    ]
