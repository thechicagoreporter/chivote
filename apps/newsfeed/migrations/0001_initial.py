# Generated by Django 2.1.5 on 2019-01-24 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0006_load_candidates_ballotready_ids'),
        ('races', '0002_load_races'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hed', models.CharField(max_length=280)),
                ('date', models.DateTimeField()),
                ('link', models.URLField()),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField()),
                ('date', models.DateTimeField()),
                ('link', models.URLField()),
                ('source', models.CharField(max_length=200)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='candidatestatement',
            name='issue',
            field=models.ManyToManyField(to='newsfeed.Issue'),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ManyToManyField(to='newsfeed.Issue'),
        ),
        migrations.AddField(
            model_name='article',
            name='race',
            field=models.ManyToManyField(to='races.Race'),
        ),
    ]
