# Generated by Django 3.2.5 on 2021-08-10 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=250)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.country')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=250)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.country')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=250)),
                ('role', models.CharField(blank=True, default='', max_length=50)),
                ('bats', models.CharField(blank=True, default='', max_length=50)),
                ('bowls', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cric.country')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.teams')),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_of_matches', models.CharField(max_length=250)),
                ('match_type', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('winner', models.CharField(blank=True, default='', max_length=10)),
                ('looser', models.CharField(blank=True, default='', max_length=10)),
                ('man_of_the_match', models.CharField(blank=True, default='', max_length=50)),
                ('bowler_of_the_match', models.CharField(blank=True, default='', max_length=50)),
                ('best_fielder', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.country')),
                ('venue_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Match_Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.country')),
                ('list_of_matches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.matches')),
                ('player_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.players')),
                ('team_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cric.teams')),
                ('venue_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.venue')),
            ],
        ),
    ]
