# Generated by Django 4.1.2 on 2022-10-26 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
