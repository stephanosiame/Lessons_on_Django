# main/views.py
import requests
from django.shortcuts import render
from django.contrib import messages

API_KEY = "2f83faca48c8e86172fa158a5057fecd"
url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"

def index(request):
    weather_data = None  # Default: no data yet
    city_name = ""

    if request.method == "POST":
        city_name = request.POST.get("city")
        if city_name:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }
            else:
                messages.error(request, f"City '{city_name}' not found.")
        else:
            messages.warning(request, "Please enter a city name.")

    context = {
        "weather": weather_data,
        "city": city_name,
        "title": "Weather App"
    }
    return render(request, "main/index.html", context)
