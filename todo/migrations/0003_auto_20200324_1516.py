# Generated by Django 2.2.4 on 2020-03-24 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='body',
            new_name='description',
        ),
    ]
