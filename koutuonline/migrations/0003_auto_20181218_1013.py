# Generated by Django 2.1.4 on 2018-12-18 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koutuonline', '0002_auto_20181218_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='height',
        ),
        migrations.RemoveField(
            model_name='img',
            name='width',
        ),
    ]