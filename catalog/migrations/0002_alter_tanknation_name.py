# Generated by Django 3.2.9 on 2021-12-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanknation',
            name='name',
            field=models.CharField(help_text='Enter a tank nation', max_length=200, null=True),
        ),
    ]
