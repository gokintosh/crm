# Generated by Django 3.0.7 on 2020-06-07 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out door', 'Out door')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]