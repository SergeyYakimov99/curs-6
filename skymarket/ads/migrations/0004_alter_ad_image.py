# Generated by Django 3.2.6 on 2022-11-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]