# Generated by Django 2.2.1 on 2019-05-03 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_update',
            new_name='date_updated',
        ),
    ]