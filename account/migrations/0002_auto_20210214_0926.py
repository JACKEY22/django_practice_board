# Generated by Django 3.1.6 on 2021-02-14 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='BasicUser',
        ),
    ]
