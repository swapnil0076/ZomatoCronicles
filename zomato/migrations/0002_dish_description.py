# Generated by Django 4.2.4 on 2023-08-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(default='Your default description here'),
        ),
    ]
