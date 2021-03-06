# Generated by Django 3.2.12 on 2022-04-02 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='movie_release_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor1_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/products/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor2_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/products/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor3_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/products/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor4_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/products/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor5_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/products/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_actor6_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/products/cast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_director1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_director2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_writer1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_writer2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tmdb',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
