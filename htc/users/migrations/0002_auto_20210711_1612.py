# Generated by Django 3.2.5 on 2021-07-11 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='last',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
