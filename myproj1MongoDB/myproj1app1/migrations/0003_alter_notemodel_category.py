# Generated by Django 5.0.4 on 2024-04-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproj1app1', '0002_notemodel_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='category',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
