# Generated by Django 3.0.8 on 2020-07-14 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Hidden',
            new_name='hidden',
        ),
    ]