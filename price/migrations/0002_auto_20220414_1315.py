# Generated by Django 3.2.12 on 2022-04-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='price_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50, unique=True)),
                ('plan_price', models.IntegerField()),
                ('plan_valid', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
