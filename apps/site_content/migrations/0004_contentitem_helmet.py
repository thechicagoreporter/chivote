# Generated by Django 2.1.5 on 2019-01-27 21:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0003_auto_20190124_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentitem',
            name='helmet',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
