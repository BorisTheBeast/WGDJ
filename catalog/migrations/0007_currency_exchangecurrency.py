# Generated by Django 3.2.9 on 2021-12-11 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20211210_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter exchange currensy', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_currensy', models.ForeignKey(help_text='Select an exchange currency for products', on_delete=django.db.models.deletion.CASCADE, to='catalog.exchangecurrency')),
            ],
        ),
    ]
