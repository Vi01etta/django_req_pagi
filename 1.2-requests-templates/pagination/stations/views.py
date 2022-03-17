from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))




def bus_stations(request):
    content = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content.append({'Name': row['Name'], 'Street': row['Street'], 'District':  row['District']})
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    page_object = page.object_list
    context = {
        'bus_stations': page_object,
        'page': page,
    }
    return render(request, 'stations/index.html', context)


