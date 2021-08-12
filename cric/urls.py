from django.urls import path, include
from cric import views

app_name = 'cric'

urlpatterns = [
    path('api/country', views.CountryList.as_view()),
    path('api/teams', views.TeamList.as_view()),
    path('api/players', views.PlayerList.as_view()),
    path('api/venue', views.VenueList.as_view()),
    path('api/matches', views.MatchList.as_view()),
    path('api/match_summary', views.MatchSummaryList.as_view()),
    path('api/batting', views.BattingList.as_view()),
    path('api/bowling', views.BowlingList.as_view()),
    path('', views.home, name='home'),
    path('team_profile/<int:id>/', views.players, name='players'),
    path('player_profile/<int:id>/', views.players_profile, name='player_profile'),
    path('venue/', views.venue, name='venue'),
    path('match/',views.matches,name = 'match'),
    path('match_summary/',views.match_summary,name = 'match_summary'),

]
