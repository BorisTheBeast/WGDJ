# Generated by Django 3.2.9 on 2021-12-20 00:23

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('catalog', '0018_prodimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='All',
            new_name='AllProducts',
        ),
    ]
