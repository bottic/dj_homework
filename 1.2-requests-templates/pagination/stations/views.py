import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    station = []
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        station_dictreader = csv.DictReader(csvfile)
        station = [row for row in station_dictreader]
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(station, 1)


    context = {
        'bus_stations': station,
        'page': paginator.get_page(page_number),
    }
    return render(request, 'stations/index.html', context)
