# Generated by Django 3.0.3 on 2020-03-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_auto_20200307_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='description',
            field=models.TextField(default='', max_length=260, verbose_name='Краткое описание о работнике'),
        ),
    ]