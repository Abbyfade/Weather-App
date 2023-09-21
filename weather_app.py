import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import requests
import signal
import time

APP_ID = "baa74facf29c069884397a4415b7dc4b"

def get_user_city():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        city = data.get('city', 'Unknown')
        return city
    except Exception as e:
        return 'Unknown'

user_city = get_user_city()

class WeatherTrayApp:
    def __init__(self):
        self.tray_icon = self.create_tray_icon()
        self.last_click_time = 0

    def create_tray_icon(self):
        tray_icon = Gtk.StatusIcon()
        tray_icon.set_from_file("weather.png")  # Replace with the path to your icon image
        tray_icon.set_tooltip_text("Weather App")
        tray_icon.connect("button-press-event", self.on_tray_button_press)
        tray_icon.connect("button-release-event", self.on_tray_button_release)
        return tray_icon

    def fetch_weather_data(self):
        try:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={APP_ID}&units=metric"
            )
            data = response.json()
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"Weather: {weather.capitalize()}\nTemperature: {temperature}°C"
        except Exception as e:
            return str(e)

    def on_tray_button_press(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 1:  # Left button press
            self.last_click_time = time.time()

    def on_tray_button_release(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_RELEASE and event.button == 1:  # Left button release
            current_time = time.time()
            if current_time - self.last_click_time < 0.5:
                weather_info = self.fetch_weather_data()
                self.show_notification("Weather Info", weather_info)

    def show_notification(self, title, message):
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
        Gtk.main_quit()

def main():
    Gtk.init([])
    app = WeatherTrayApp()
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Handle Ctrl+C gracefully
    Gtk.main()

if __name__ == "__main__":
    main()
