# Generated by Django 4.2 on 2023-04-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instock',
            field=models.BooleanField(null=True),
        ),
    ]
