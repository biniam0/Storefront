# Generated by Django 5.1 on 2024-10-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20241027_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birth_day',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='memebership',
            new_name='membership',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='name',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='unit_price',
            field=models.FloatField(default=0),
        ),
    ]
