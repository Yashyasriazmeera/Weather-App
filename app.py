import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_current_weather(city: str) -> dict | None:
    """Fetch current weather data for the given city."""
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        return None
    if response.status_code == 200:
        return response.json()
    return None


def get_forecast(city: str) -> list[dict] | None:
    """Fetch a 5-day / 3-hour forecast and return one entry per day."""
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        return None
    if response.status_code != 200:
        return None

    data = response.json()
    daily: dict[str, dict] = {}

    for entry in data.get("list", []):
        date_str = entry["dt_txt"].split(" ")[0]
        if date_str not in daily:
            daily[date_str] = entry

    # Return the next 5 distinct days in chronological order
    return [v for _, v in sorted(daily.items())][:5]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            current = get_current_weather(city)
            forecast = get_forecast(city)

            if current is None:
                if not API_KEY:
                    error = "No API key configured. Please set the OPENWEATHER_API_KEY environment variable."
                else:
                    error = f"Could not retrieve weather for '{city}'. Check the city name or try again later."
                return render_template("index.html", error=error, city=city)

            return render_template(
                "weather.html",
                city=city,
                current=current,
                forecast=forecast or [],
            )

    return render_template("index.html")


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug)
