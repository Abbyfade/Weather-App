import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import requests
import signal
import time

# Replace with your Weatherstack API key
API_ID = "fc86edb97615691828d6086e50a9810e"

def get_user_city():
    try:
        # Use the ipinfo.io API to get the user's city based on their IP address
        response = requests.get('https://ipinfo.io')
        data = response.json()
        city = data.get('city', 'Unknown')
        return city
    except Exception as e:
        return 'Unknown'

# Get the user's city using the function above
user_city = get_user_city()

class WeatherTrayApp:
    def __init__(self):
        # Initialize the application and tray icon
        self.tray_icon = self.create_tray_icon()
        self.last_click_time = 0

    def create_tray_icon(self):
        # Create and configure the system tray icon
        tray_icon = Gtk.StatusIcon()
        tray_icon.set_from_file("weather.png")  # Replace with the path to your icon image
        tray_icon.set_tooltip_text("Weather App")
        tray_icon.connect("button-press-event", self.on_tray_button_press)
        tray_icon.connect("button-release-event", self.on_tray_button_release)
        return tray_icon

    def fetch_weather_data(self):
        try:
            # Make a GET request to the Weatherstack API to fetch weather data for the user's city
            response = requests.get(
                f"http://api.weatherstack.com/current?access_key={API_ID}&query={user_city}"
            )
        
            # Check if the request was successful (HTTP status code 200)
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

    def on_tray_button_press(self, widget, event):
        # Handle left button press event
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 1:
            self.last_click_time = time.time()

    def on_tray_button_release(self, widget, event):
        # Handle left button release event
        if event.type == Gdk.EventType.BUTTON_RELEASE and event.button == 1:
            current_time = time.time()
            if current_time - self.last_click_time < 0.5:
                weather_info = self.fetch_weather_data()
                self.show_notification("Weather Info", weather_info)

    def show_notification(self, title, message):
        # Display a notification dialog with the weather information
        dialog = Gtk.MessageDialog(
            transient_for=None,
            flags=0,
            type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.CLOSE,
            message_format=f"{title}\n\n{message}"
        )
        dialog.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        dialog.run()
        dialog.destroy()

    def quit(self):
        # Quit the GTK application
        Gtk.main_quit()

def main():
    # Initialize the GTK application and start the WeatherTrayApp
    Gtk.init([])
    app = WeatherTrayApp()
    
    # Handle Ctrl+C gracefully to quit the application
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    # Start the GTK main loop
    Gtk.main()

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
