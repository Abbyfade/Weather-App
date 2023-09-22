from flask import Flask, render_template
import weather_app  # Import your GTK weather app code

app = Flask(__name__)

@app.route('/')
def index():
    # Add code to interact with your GTK weather app here
    # Fetch weather data and return it as HTML
    weather_info = weather_app.get_weather_data()
    return render_template('index.html', weather=weather_info)

if __name__ == '__main__':
    app.run()
