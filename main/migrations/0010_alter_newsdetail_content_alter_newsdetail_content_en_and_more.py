# Generated by Django 4.1.2 on 2023-06-19 11:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_news_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdetail',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsdetail',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsdetail',
            name='content_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsdetail',
            name='content_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsdetail',
            name='content_uz',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]