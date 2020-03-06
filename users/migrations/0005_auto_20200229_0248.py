# Generated by Django 3.0.3 on 2020-02-28 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='job',
        ),
        migrations.AddField(
            model_name='users',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Jobs'),
            preserve_default=False,
        ),
    ]
