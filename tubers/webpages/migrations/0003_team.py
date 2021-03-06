# Generated by Django 3.1.4 on 2021-05-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_slider_button_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=100)),
                ('fb_link', models.URLField(blank=True, max_length=255)),
                ('insta_link', models.URLField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
