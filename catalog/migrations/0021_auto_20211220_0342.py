# Generated by Django 3.2.9 on 2021-12-20 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_allproducts_prod_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allproducts',
            name='nation',
            field=models.ForeignKey(blank=True, help_text='Select a nation for this tank', on_delete=django.db.models.deletion.CASCADE, to='catalog.tanknation'),
        ),
        migrations.AlterField(
            model_name='allproducts',
            name='prod_type',
            field=models.ManyToManyField(help_text='Select a type of your product', to='catalog.ProdType'),
        ),
        migrations.AlterField(
            model_name='allproducts',
            name='type',
            field=models.ManyToManyField(blank=True, help_text='Select a type for this tank', to='catalog.TankType'),
        ),
    ]
