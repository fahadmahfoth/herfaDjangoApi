# Generated by Django 3.0.3 on 2020-03-01 00:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200229_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
