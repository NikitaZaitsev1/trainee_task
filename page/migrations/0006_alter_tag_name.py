# Generated by Django 4.1.2 on 2022-10-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
