# Generated by Django 3.0.2 on 2021-02-13 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_auto_20210214_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]