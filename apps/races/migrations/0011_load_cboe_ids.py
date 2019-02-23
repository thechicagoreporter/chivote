# Generated by Django 2.1.7 on 2019-02-23 17:02

from django.db import migrations


def load_cboe_ids(apps, schema_editor):
    import re

    Race = apps.get_model('races', 'Race')

    Race.objects.filter(slug='city-mayor').update(cboe_id='0010')
    Race.objects.filter(slug='city-clerk').update(cboe_id='0011')
    Race.objects.filter(slug='city-treasurer').update(cboe_id='0012')

    for r in Race.objects.filter(slug__iendswith='alderman'):
        ward_no = re.search(r'\d+', r.slug).group()
        cboe_id = '00' + str(12 + int(ward_no))  # e.g. 1st ward => 0013
        r.cboe_id = cboe_id
        r.save()


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0010_race_cboe_id'),
    ]

    operations = [
        migrations.RunPython(load_cboe_ids,
                             reverse_code=migrations.RunPython.noop),
    ]
