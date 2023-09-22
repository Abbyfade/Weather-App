from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_ID = "fc86edb97615691828d6086e50a9810e"

def get_weather_data(city):
    try:
        response = requests.get(
            f"http://api.weatherstack.com/current?access_key={API_ID}&query={city}"
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            if "current" in data:
                weather = data["current"]["weather_descriptions"][0]
                temperature = data["current"]["temperature"]
                return f"Weather: {weather}\nTemperature: {temperature}°C"
            else:
                return "Weather data not available."
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    weather_info = get_weather_data(city)
    return render_template('index.html', weather=weather_info, city=city)

if __name__ == '__main__':
    app.run()
