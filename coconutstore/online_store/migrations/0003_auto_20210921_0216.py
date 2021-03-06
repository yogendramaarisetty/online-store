# Generated by Django 3.2.7 on 2021-09-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_auto_20210921_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverypartner',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='FullName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='IsActive',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='IsVerified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='Otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='ProfilePic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
