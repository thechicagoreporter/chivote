# Generated by Django 2.0 on 2018-10-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20181031_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Format: YYYY-MM-DD', null=True, verbose_name='born'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, help_text='Format: YYYY-MM-DD', null=True, verbose_name='died'),
        ),
    ]
