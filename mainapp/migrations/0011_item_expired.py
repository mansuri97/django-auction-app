# Generated by Django 2.2.5 on 2019-11-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_item_bidders'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
