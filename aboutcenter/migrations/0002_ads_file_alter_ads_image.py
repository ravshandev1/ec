# Generated by Django 4.1.2 on 2023-06-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutcenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]