# Generated by Django 5.1 on 2024-10-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_orderitem_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotion',
            old_name='dicount',
            new_name='discount',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='cart',
        ),
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
