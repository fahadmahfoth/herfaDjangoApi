# Generated by Django 3.0.3 on 2020-02-28 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200229_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='job',
        ),
    ]
