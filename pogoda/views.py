from django.shortcuts import render
import requests
from .models import Miasto
from .forms import MiastoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=bbd6e611f8aab0b20331ccfbde67cd30"
    cities = Miasto.objects.order_by('date_added')
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'miasto': city.nazwa,
            'temperatura': r['main']['temp'],
            'opis': r['weather'][0]['description'],
            'ikona': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    if request.method != 'POST':
        form = MiastoForm()
    else:
        form = MiastoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pogoda:index'))


    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'pogoda/index.html', context)