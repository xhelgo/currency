# Generated by Django 4.1.7 on 2023-03-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'US Dollar'), (2, 'Euro'), (3, 'British Pound'), (4, 'Polish Zloty'), (5, 'Swiss Franc'), (6, 'Japanese Yen'), (7, 'Canadian Dollar'), (8, 'Australian Dollar')], default=1),
        ),
    ]