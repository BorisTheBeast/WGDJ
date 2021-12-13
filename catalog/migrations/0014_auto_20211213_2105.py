# Generated by Django 3.2.9 on 2021-12-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20211213_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gold',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='premium',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='gold',
            name='sort_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='premium',
            name='sort_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
