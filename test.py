from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            print(f"\n🌍 Погода в {city}:")
            print(f"🌡️  Температура: {temp}°C (ощущается как {feels_like}°C)")
            print(f"☁️  {description}")
            print(f"💧 Влажность: {humidity}%")
            print(f"💨 Ветер: {wind} м/с")
        else:
            print("Город не найден!")
    except Exception:
        print("Нет подключения к интернету!")

while True:
    city = input("\nВведи город (или 'выход'): ")
    if city.lower() == "выход":
        break
    get_weather(city)