from flask import Flask, render_template
import requests

app = Flask(__name__)

API_ID = "fc86edb97615691828d6086e50a9810e"

def get_user_city():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        city = data.get('city', 'Unknown')
        return city
    except Exception as e:
        return 'Unknown'

user_city = get_user_city()

def get_weather_data():
    response = requests.get(
            f"http://api.weatherstack.com/current?access_key={API_ID}&query={user_city}")
        
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            weather = data["current"]["weather_descriptions"][0]
            temperature = data["current"]["temperature"]
            return f"Weather: {weather}\nTemperature: {temperature}°C"
        else:
            return "Weather data not available."


@app.route('/')
def index():
    # Add code to interact with your GTK weather app here
    # Fetch weather data and return it as HTML
    weather_info = get_weather_data()
    return render_template('index.html', weather=weather_info)

if __name__ == '__main__':
    app.run()
