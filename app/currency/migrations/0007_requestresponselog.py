# Generated by Django 4.1.7 on 2023-03-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_contactus_options_contactus_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request', models.CharField(max_length=32)),
            ],
        ),
    ]
