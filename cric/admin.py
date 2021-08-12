from django.contrib import admin
from .models import Country, Teams, Venue, Players, Matches, Match_Summary,Batting,Bowling

# Register your models here


admin.site.register(Country)
admin.site.register(Teams)
admin.site.register(Venue)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(Match_Summary)
admin.site.register(Batting)
admin.site.register(Bowling)

