# Generated by Django 4.2.1 on 2023-10-10 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo',
            new_name='todo_list',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='wish',
            new_name='wish_list',
        ),
    ]