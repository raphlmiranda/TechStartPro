# Generated by Django 3.1.2 on 2020-10-28 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olist', '0002_auto_20201028_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('value', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olist.category')),
            ],
        ),
    ]