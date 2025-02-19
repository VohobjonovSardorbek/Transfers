
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('clubs/', ClubView.as_view(), name='clubs'),
    path('clubs/<int:pk>/details/', Club_details_View.as_view(), name='clubs_details'),
    path('countries/<int:pk>/clubs/', Club_by_countryView.as_view(), name='club_by_country'),
    path('latest-transfers/', LatestTransfersView.as_view(), name="latest-transfers"),
    path('players/', PlayersView.as_view(), name='players'),
    path('young_players/', YoungPlayersView.as_view(), name='young_players'),
    path('tryouts/', TryoutsView.as_view(), name='tryouts'),
    path('about/', AboutsView.as_view(), name='about'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('expendture/', Club_expendtureView.as_view(), name='expendture'),
    path('transfer_records/', TransferRecordView.as_view(), name='transfer_records'),
    path('top-50-clubs-by-income-in-2021/', ClubIncomeView.as_view(), name='top-50-clubs-by-income-in-2021'),
    path('accurate/', AccurateView.as_view(), name='accurate'),
    path('transfer_archive/', Transfer_archiveView.as_view(), name='transfer_archive'),
    path('season/<int:pk>/', SeasonView.as_view(), name='season'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)