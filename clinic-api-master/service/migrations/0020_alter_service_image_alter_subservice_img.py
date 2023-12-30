# Generated by Django 4.1.7 on 2023-04-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_alter_service_id_alter_subservice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, default='subservice/default.svg', null=True, upload_to='service/'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='img',
            field=models.FileField(blank=True, default='subservice/default.svg', null=True, upload_to='subservice/'),
        ),
    ]