# Generated by Django 3.2.12 on 2022-04-11 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marks', '0003_remove_markitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='markitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
