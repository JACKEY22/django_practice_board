# Generated by Django 3.1.6 on 2021-02-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='이름')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='가입일자')),
            ],
            options={
                'db_table': 'basic_01_user',
            },
        ),
    ]