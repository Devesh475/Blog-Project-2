# Generated by Django 3.0.2 on 2021-02-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_blogpost_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]