# Generated by Django 4.1.13 on 2024-05-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicelistmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
