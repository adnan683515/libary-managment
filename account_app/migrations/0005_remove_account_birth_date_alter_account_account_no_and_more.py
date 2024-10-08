# Generated by Django 5.0.6 on 2024-08-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_alter_account_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
