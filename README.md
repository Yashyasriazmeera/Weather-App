# Weather-App

Simple weather forecast application using Flask and OpenWeather API.

## Features

- 🌡 **Current weather** — temperature, feels-like, humidity, wind speed, pressure
- 📅 **5-day forecast** — one snapshot per day with icon, temperature, and conditions
- ⚠️ Friendly error messages when a city is not found or the API is unreachable

## Setup

1. **Clone the repository and install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Get an API key**

   Sign up for a free API key at [openweathermap.org](https://openweathermap.org/api).

3. **Configure environment variables**

   ```bash
   cp .env.example .env
   # Edit .env and set OPENWEATHER_API_KEY=<your key>
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

   Then open <http://127.0.0.1:5000> in your browser.

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `OPENWEATHER_API_KEY` | Your OpenWeatherMap API key (**required**) | — |
| `FLASK_DEBUG` | Enable debug mode (`true`/`false`) | `false` |
