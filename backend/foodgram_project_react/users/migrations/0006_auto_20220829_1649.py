# Generated by Django 2.2.19 on 2022-08-29 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220829_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
