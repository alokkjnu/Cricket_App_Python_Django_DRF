from rest_framework import serializers
from .models import Country, Teams, Players, Matches, Match_Summary, Venue, Batting, Bowling


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country']


class TeamSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')

    class Meta:
        model = Teams
        fields = ['id', 'country', 'team_name']


class PlayerSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')
    team_name = serializers.ReadOnlyField(source='team_name.team_name')

    class Meta:
        model = Players
        fields = ['id', 'country', 'team_name', 'player_name', 'role', 'bats', 'bowls']


class VenueSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')

    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'city', 'state', 'country']


class Match_Serializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')
    venue_name = serializers.ReadOnlyField(source='venue_name.venue_name')

    class Meta:
        model = Matches
        fields = ['id', 'country', 'team1', 'team2', 'venue_name', 'list_of_matches', 'match_type', 'start_date',
                  'end_date', 'winner',
                  'looser',
                  'man_of_the_match', 'bowler_of_the_match', 'best_fielder']


class Batting_Serialize(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')
    team_name = serializers.ReadOnlyField(source='team_name.team_name')
    player_name = serializers.ReadOnlyField(source='player_name.player_name')
    venue_name = serializers.ReadOnlyField(source='venue_name.venue_name')
    list_of_matches = serializers.ReadOnlyField(source='list_of_matches.list_of_matches')
    #team = serializers.ReadOnlyField(source='country.country')

    class Meta:
        model = Batting
        fields = ['id', 'country', 'team_name', 'player_name', 'venue_name', 'list_of_matches', 'team', 'run', 'balls',
                  'four', 'six', 'sr']


class Bowling_Serialize(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')
    team_name = serializers.ReadOnlyField(source='team_name.team_name')
    player_name = serializers.ReadOnlyField(source='player_name.player_name')
    venue_name = serializers.ReadOnlyField(source='venue_name.venue_name')
    list_of_matches = serializers.ReadOnlyField(source='list_of_matches.list_of_matches')
    #team = serializers.ReadOnlyField(source='country.country')

    class Meta:
        model = Bowling
        fields = ['id', 'country', 'team_name', 'player_name', 'venue_name', 'list_of_matches', 'team','overs','median','run','wicket','economy']


class Match_Summary_Serializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.country')
    team_name = serializers.ReadOnlyField(source='team_name.team_name')
    player_name = serializers.ReadOnlyField(source='player_name.player_name')
    venue_name = serializers.ReadOnlyField(source='venue_name.venue_name')
    list_of_matches = serializers.ReadOnlyField(source='list_of_matches.list_of_matches')

    class Meta:
        model = Match_Summary
        fields = ['id', 'country', 'team_name', 'player_name', 'venue_name', 'list_of_matches']
