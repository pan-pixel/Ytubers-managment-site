# Generated by Django 3.1.4 on 2021-05-29 19:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210530_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
