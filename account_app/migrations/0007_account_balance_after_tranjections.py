# Generated by Django 5.0.6 on 2024-08-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0006_account_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance_after_tranjections',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
