# Generated by Django 4.1.13 on 2024-05-08 15:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0003_alter_invoicelistmodel_invoiceno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicelistmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='invoicelistmodel',
            name='invoiceNo',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
