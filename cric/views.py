from django.shortcuts import render, get_object_or_404
from rest_framework import generics
import requests
from .models import Country, Matches, Teams, Players, Venue, Match_Summary, Batting, Bowling
from .serializers import CountrySerializer, TeamSerializer, PlayerSerializer, VenueSerializer, Match_Serializer, \
    Match_Summary_Serializer, Batting_Serialize, Bowling_Serialize


# Create your views here.

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class TeamList(generics.ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class PlayerList(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer


class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class MatchList(generics.ListAPIView):
    queryset = Matches.objects.all()
    serializer_class = Match_Serializer


class BattingList(generics.ListAPIView):
    queryset = Batting.objects.all()
    serializer_class = Batting_Serialize


class BowlingList(generics.ListAPIView):
    queryset = Bowling.objects.all()
    serializer_class = Bowling_Serialize


class MatchSummaryList(generics.ListAPIView):
    queryset = Match_Summary.objects.all()
    serializer_class = Match_Summary_Serializer


def home(request):
    # country = get_object_or_404(Country,id=country_id)
    r = requests.get('http://127.0.0.1:8000/api/country')
    country = r.json()
    return render(request, 'cric/home.html', {'country': country})


def players(request, id):
    country = get_object_or_404(Country, id=id)
    r = requests.get('http://127.0.0.1:8000/api/players')
    r2 = requests.get('http://127.0.0.1:8000/api/teams')
    players = r.json()
    team = r2.json()
    return render(request, 'cric/players.html', {'team': team, 'players': players, 'country': country})


def players_profile(request, id):
    player = get_object_or_404(Players, id=id)
    r = requests.get('http://127.0.0.1:8000/api/players')
    players = r.json()
    return render(request, 'cric/player_profile.html', {'players': players, 'player': player})


def venue(request):
    r = requests.get('http://127.0.0.1:8000/api/venue')
    venue = r.json()
    return render(request, 'cric/venue.html', {'venue': venue})


def matches(request):
    r = requests.get('http://127.0.0.1:8000/api/matches')
    # r2 = requests.get('http://127.0.0.1:8000/api/match_summary')
    match_list = r.json()
    # match_summary = r2.json()
    return render(request, 'cric/match.html', {'match': match_list})


def match_summary(request):
    #country = get_object_or_404(Country)
    t = requests.get('http://127.0.0.1:8000/api/teams')
    r = requests.get('http://127.0.0.1:8000/api/batting')
    r2 = requests.get('http://127.0.0.1:8000/api/bowling')
    r3 = requests.get('http://127.0.0.1:8000/api/matches')
    c = requests.get('http://127.0.0.1:8000/api/country')
    match = r3.json()
    bat = r.json()
    ball = r2.json()
    team = t.json()
    country = c.json()
    return render(request, 'cric/match_summary.html', {'match': match, 'bat': bat, 'ball': ball, 'team': team,'country':country})
