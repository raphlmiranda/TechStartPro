# Generated by Django 3.1.2 on 2020-10-29 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olist', '0005_csv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='specifications',
            new_name='csvFile',
        ),
    ]
