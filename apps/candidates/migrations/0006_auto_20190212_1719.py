# Generated by Django 2.1.5 on 2019-02-12 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_auto_20190131_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='ri_cash_on_hand',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='ri_funds_raised_this_cycle',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='ri_last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]