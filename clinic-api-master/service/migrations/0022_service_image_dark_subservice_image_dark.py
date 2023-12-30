# Generated by Django 4.1.7 on 2023-05-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_rename_image_service_image_light_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image_dark',
            field=models.FileField(blank=True, default='subservice/default.svg', null=True, upload_to='service/'),
        ),
        migrations.AddField(
            model_name='subservice',
            name='image_dark',
            field=models.FileField(blank=True, default='subservice/default.svg', null=True, upload_to='subservice/'),
        ),
    ]