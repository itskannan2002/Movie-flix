# Generated by Django 3.2.12 on 2022-04-15 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220409_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='movie_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
    ]
