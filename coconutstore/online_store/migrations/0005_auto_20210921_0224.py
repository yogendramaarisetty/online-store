# Generated by Django 3.2.7 on 2021-09-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0004_auto_20210921_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='FullName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
