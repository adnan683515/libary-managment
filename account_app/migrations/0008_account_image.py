# Generated by Django 5.0.6 on 2024-08-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0007_account_balance_after_tranjections'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='picture/'),
        ),
    ]
