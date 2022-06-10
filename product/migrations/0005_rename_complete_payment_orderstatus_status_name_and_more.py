# Generated by Django 4.0.5 on 2022-06-10 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_orderstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderstatus',
            old_name='complete_payment',
            new_name='status_name',
        ),
        migrations.RemoveField(
            model_name='orderstatus',
            name='order_cancel',
        ),
        migrations.RemoveField(
            model_name='orderstatus',
            name='order_complete',
        ),
        migrations.RemoveField(
            model_name='orderstatus',
            name='shipping_complete',
        ),
        migrations.RemoveField(
            model_name='orderstatus',
            name='shipping_start',
        ),
    ]