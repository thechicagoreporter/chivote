# Generated by Django 2.1.5 on 2019-02-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0009_auto_20190208_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentitem',
            name='helmet_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='helmet_es',
            field=models.TextField(blank=True, null=True),
        ),
    ]