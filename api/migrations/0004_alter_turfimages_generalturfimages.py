# Generated by Django 3.2.9 on 2022-08-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_turfimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turfimages',
            name='generalTurfImages',
            field=models.ImageField(blank=True, default='esp32-cam.jpg', null=True, upload_to='media/images'),
        ),
    ]
