import logging
import logging.handlers
import os
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 31.20,  # Alexandria Latitude
        "longitude": 29.92,  # Alexandria Longitude
        "current_weather": True
    }

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()  # Raises an error for 4xx/5xx status codes

        data = r.json()
        temperature = data["current_weather"]["temperature"]
        logger.info(f'Weather in Alexandria: {temperature}°C')

    except requests.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
