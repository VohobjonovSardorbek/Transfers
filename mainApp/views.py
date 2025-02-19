from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import F, Func, FloatField
from .models import *
from django.db.models import Sum

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context = {
            "clubs" : clubs
        }
        return render(request, 'clubs.html', context)


class LatestTransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-datetime')
        context = {
            "transfers" : transfers
        }
        return render(request, 'latest-transfers.html', context)


class PlayersView(View):
    def get(self, request):
        players = Player.objects.order_by('-price')
        context = {
            "players" : players
        }
        return render(request, 'players.html', context)


class YoungPlayersView(View):
    def get(self, request):
        players = Player.objects.filter(age__lte=20).order_by('-price')
        context = {
            "players" : players
        }
        return render(request, 'young_players.html', context)


class TryoutsView(View):
    def get(self, request):
        return render(request, 'tryouts.html')


class AboutsView(View):
    def get(self, request):
        return render(request, 'about.html')


class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')


class AccurateView(View):
    def get(self, request):
        transfers = Transfer.objects.annotate(
            price_difference=Func(F('price') - F('price_tft'), function='ABS', output_field=FloatField())
        ).order_by('price_difference')
        context = {
            "transfers" : transfers,
        }
        return render(request, 'stats/accurate.html', context)


class Club_by_countryView(View):
    def get(self, request, pk):
        country = get_object_or_404(Country, id=pk)
        clubs = Club.objects.filter(country__name=country.name)
        context = {
            "clubs" : clubs,
            "country" : country
        }
        return render(request, 'club_by_country.html', context)


class Club_details_View(View):
    def get(self, request, pk):
        club = get_object_or_404(Club, id=pk)
        players = Player.objects.filter(club__name=club.name)
        context = {
            "club" : club,
            "players" : players
        }
        return render(request, 'country-clubs.html', context)


class Club_expendtureView(View):
    def get(self, request):
        # Eng ko'p pul sarflagan klublarni saralash
        clubs_with_highest_spending = Club.objects.annotate(
            total_spent=Sum('club_to_set__price')
        ).order_by('-total_spent')
        context = {
            "clubs_with_highest_spending" : clubs_with_highest_spending
        }
        return render(request, 'stats/expendture.html', context)


class TransferRecordView(View):
    def get(self, request):
        transfers = Transfer.objects.order_by('-price')
        context = {
            "transfers" : transfers
        }
        return render(request, 'stats/transfer-records.html', context)


class ClubIncomeView(View):
    def get(self, request):
        club_incomes = Club.objects.annotate(
            total_income=Sum('club_from_set__price')
        ).order_by('-total_income')
        print(club_incomes)
        context = {
            "club_incomes" : club_incomes
        }
        return render(request, 'stats/top-50-clubs-by-income-in-2021.html', context)


class Transfer_archiveView(View):
    def get(self, request):
        seasons = Season.objects.all()
        context = {
            "seasons" : seasons
        }
        return render(request, 'transfer-archive.html', context)


class SeasonView(View):
    def get(self, request, pk):
        season = get_object_or_404(Season, id=pk)
        transfers = Transfer.objects.filter(season__name=season.name)
        print(Season.objects.all( ))
        context = {
            "transfers" : transfers
        }
        return render(request, '2017-18season.html', context)