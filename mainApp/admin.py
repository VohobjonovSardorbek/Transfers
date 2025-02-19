from django.contrib import admin
from django.utils.html import format_html
from .models import *


class SeasonAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_image', 'president', 'coach', 'found_date', 'country']
    list_filter = ['country']
    search_fields = ['name', 'president', 'coach']
    ordering = ('name', )

    def get_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="32" height="32" style="border-radius: 5px;"/>'.format(obj.image.url))
        return "No Image"

    get_image.short_description = "Preview"


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'position', 'country', 'price',  'club']
    list_filter = ['country', 'club', 'position', 'age']
    search_fields = ['name']
    ordering = ['name', 'price']


class TransferAdmin(admin.ModelAdmin):
    list_display = ['player', 'club_from', 'club_to', 'season', 'price', 'price_tft', 'datetime']
    list_filter = ['player', 'club_from', 'club_to', 'season']
    ordering = ('datetime', )
    search_fields = ['player__name']


admin.site.register(Season, SeasonAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Transfer, TransferAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', '']