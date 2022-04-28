# Generated by Django 3.2.12 on 2022-04-26 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220425_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='movie_download_link_1080p',
            field=models.URLField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='movie_download_link_720p',
            field=models.URLField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
    ]
