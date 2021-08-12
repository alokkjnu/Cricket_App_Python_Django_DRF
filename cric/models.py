from django.db import models


# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=250)

    def __str__(self):
        return self.country


class Teams(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=250)

    def __str__(self):
        return self.team_name


class Players(models.Model):
    team_name = models.ForeignKey(Teams, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default='')
    player_name = models.CharField(max_length=250)
    role = models.CharField(max_length=50, default='', blank=True)
    bats = models.CharField(max_length=50, default='', blank=True)
    bowls = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.player_name



class Venue(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    venue_name = models.CharField(max_length=250)
    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.venue_name


class Matches(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # team_name = models.ForeignKey(Teams, on_delete=models.CASCADE)
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE)
    # player_name = models.ForeignKey(Players, on_delete=models.CASCADE)
    team1 = models.ForeignKey('Country',on_delete=models.CASCADE,blank=True, related_name='team_1',null=True)
    team2 = models.ForeignKey('Country',on_delete=models.CASCADE,blank=True,related_name='team_2',null=True)
    list_of_matches = models.CharField(max_length=250)
    match_type = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    winner = models.CharField(max_length=10, default='', blank=True)
    looser = models.CharField(max_length=10, default='', blank=True)
    man_of_the_match = models.CharField(max_length=50, default='', blank=True)
    bowler_of_the_match = models.CharField(max_length=50, default='', blank=True)
    best_fielder = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.list_of_matches


class Batting(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Teams, on_delete=models.CASCADE, default='')
    player_name = models.ForeignKey(Players, on_delete=models.CASCADE)
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE)
    list_of_matches = models.ForeignKey(Matches, on_delete=models.CASCADE)
    team = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, related_name='team1', null=True)
    #team2 = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, related_name='team2', null=True)
    run = models.IntegerField(blank=True, default='', null=True)
    balls = models.IntegerField(blank=True, default='')
    four = models.IntegerField(blank=True, default='')
    six = models.IntegerField(blank=True, default='')
    sr = models.FloatField(blank=True, default='')

    def __str__(self):
        return str(self.player_name)


class Bowling(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Teams, on_delete=models.CASCADE, default='')
    player_name = models.ForeignKey(Players, on_delete=models.CASCADE)
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE)
    list_of_matches = models.ForeignKey(Matches, on_delete=models.CASCADE)
    team = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, related_name='t1', null=True)
    #team2 = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, related_name='t2', null=True)
    overs = models.FloatField(blank=True, default='')
    median = models.IntegerField(blank=True, default='')
    run = models.IntegerField(blank=True, default='')
    wicket = models.IntegerField(blank=True, default='')
    economy = models.FloatField(blank=True, default='')

    def __str__(self):
        return str(self.player_name)


class Match_Summary(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Teams, on_delete=models.CASCADE, default='')
    player_name = models.ForeignKey(Players, on_delete=models.CASCADE)
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE)
    list_of_matches = models.ForeignKey(Matches, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.list_of_matches)
