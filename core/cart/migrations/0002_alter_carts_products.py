# Generated by Django 3.2.6 on 2021-09-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='products',
            field=models.CharField(max_length=50),
        ),
    ]
