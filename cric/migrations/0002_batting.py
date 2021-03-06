# Generated by Django 3.2.5 on 2021-08-10 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.IntegerField(blank=True, default='')),
                ('balls', models.IntegerField(blank=True, default='')),
                ('four', models.IntegerField(blank=True, default='')),
                ('six', models.IntegerField(blank=True, default='')),
                ('sr', models.FloatField(blank=True, default='')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.country')),
                ('list_of_matches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.matches')),
                ('player_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.players')),
                ('team_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cric.teams')),
                ('venue_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cric.venue')),
            ],
        ),
    ]
