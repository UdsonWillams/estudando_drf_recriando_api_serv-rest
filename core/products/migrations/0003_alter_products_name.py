# Generated by Django 3.2.6 on 2021-09-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
