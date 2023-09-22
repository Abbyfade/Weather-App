---

# GTK System Tray Weather Application

This is a small system tray application built using GTK-3 that provides you with weather information for your city. You can access weather details by double-clicking the system tray icon.

## Features

- Displays current weather information (description and temperature) for your city.
- Double-click the system tray icon to fetch and display weather data.
- Minimalistic design with a system tray icon.

## Prerequisites

Before running this application, make sure you have the following prerequisites installed:

- Python 3
- GTK-3 (Python bindings)
- The `requests` library for fetching weather data.

You can install the required libraries using pip:

```bash
pip install pygobject requests
```
If you are having issues installing using pip, click on this article to see how to install pygobject on your computer.
https://pygobject.readthedocs.io/en/latest/getting_started.html

## Usage

1. Clone this repository to your local machine or download the source code.

2. Replace `"weather.png"` in the `create_tray_icon` method with the path to your custom tray icon image (optional).

3. Run the application using Python:

```bash
python weather_app.py
```

4. The application will appear as a system tray icon. Double-click the icon to fetch and display weather information for your city.

## Configuration

You can configure the application by modifying the following variables in the code:

- `API_ID`: Replace with your Weatherstack API key.

## Troubleshooting

If you encounter any issues or errors while running the application, please check your Python environment and library installations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
