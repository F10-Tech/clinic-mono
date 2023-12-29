# Generated by Django 4.1.7 on 2023-12-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_patient_img_1_patient_img_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='img_1',
            field=models.FileField(blank=True, default='images/subservice/default.svg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='img_2',
            field=models.FileField(blank=True, default='images/subservice/default.svg', null=True, upload_to='images/'),
        ),
    ]
