# Generated by Django 2.1.5 on 2019-01-27 22:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0005_auto_20190127_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentitem',
            name='background',
            field=colorfield.fields.ColorField(default='#31313B', max_length=18),
        ),
    ]
