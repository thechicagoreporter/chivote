# Generated by Django 2.1.5 on 2019-01-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_load_candidates_and_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['ballot_order']},
        ),
        migrations.AlterField(
            model_name='candidate',
            name='ballot_order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='br_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='isbe_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='ri_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]