# Generated by Django 5.0.6 on 2024-08-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_alter_account_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
