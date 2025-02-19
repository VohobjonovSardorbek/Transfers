from .models import *

def country_list(request):
    countries = Country.objects.filter(club__isnull=False).order_by('name').distinct()

    unique_countries = list({c.name: c for c in countries}.values())

    mid = len(unique_countries) // 2
    if mid // 2 == 1:
        country_left = unique_countries[:mid + 1]
        country_right = unique_countries[mid + 1:]
    else:
        country_left = unique_countries[:mid]
        country_right = unique_countries[mid:]

    return {'country_left': country_left, 'country_right': country_right}
