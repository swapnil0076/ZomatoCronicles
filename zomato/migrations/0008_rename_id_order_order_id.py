# Generated by Django 4.2.4 on 2023-08-16 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0007_rename_order_id_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='order_id',
        ),
    ]
