# Generated by Django 3.1.6 on 2021-02-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210214_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicuser',
            options={'verbose_name': '기본 사용자', 'verbose_name_plural': '기본 사용자'},
        ),
        migrations.AddField(
            model_name='basicuser',
            name='email',
            field=models.EmailField(default=1, max_length=128, verbose_name='이메일'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicuser',
            name='username',
            field=models.CharField(max_length=64, verbose_name='계정명'),
        ),
    ]
