# Generated by Django 3.2.9 on 2021-12-09 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_tank_tier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tank',
            name='nation',
        ),
        migrations.AddField(
            model_name='tank',
            name='nation',
            field=models.ForeignKey(default=2, help_text='Select a nation for this tank', on_delete=django.db.models.deletion.CASCADE, to='catalog.tanknation'),
            preserve_default=False,
        ),
    ]
