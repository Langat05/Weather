from django.shortcuts import render
import urllib.request
import json

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city +
            '&units=metric&appid=ca6424e3c416be4ac9b9e5ae49abd2dd').read()
        list_of_data = json.loads(source)
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ',',
            'temp': str(list_of_data['main']['temp']) + '°C',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': str(list_of_data['weather'][0]['icon']),
            'speed': str(list_of_data['wind']['speed'])
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)