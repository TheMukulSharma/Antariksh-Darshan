"""Location detection: IP-based auto-detection with manual fallback."""

import pytz
import requests


def get_valid_float(prompt_text, min_val, max_val):
    """Prompt until the user enters a float within [min_val, max_val]."""
    while True:
        try:
            val = float(input(prompt_text))
            if min_val <= val <= max_val:
                return val
            print(f"Error: Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid numeric input. Please try again.")


def get_valid_timezone(prompt):
    """Prompt until the user enters a valid IANA timezone name."""
    while True:
        tz_input = input(prompt).strip()
        try:
            return pytz.timezone(tz_input).zone
        except pytz.UnknownTimeZoneError:
            print("Error: Unknown timezone.")


def get_location():
    """Detect the user's location via IP, falling back to manual entry."""
    try:
        response = requests.get("https://ipwho.is/", timeout=5)
        data = response.json()
        if not data["success"]:
            raise ValueError("API returned failure status")
        return {
            "lat": data["latitude"],
            "lon": data["longitude"],
            "timezone": data["timezone"]["id"],
            "city": data["city"],
            "country": data["country"],
        }

    except Exception:
        print("\nAuto-detection failed. Enter manually:")
        lat = get_valid_float("Latitude (-90 to 90): ", -90.0, 90.0)
        lon = get_valid_float("Longitude (-180 to 180): ", -180.0, 180.0)
        tz = get_valid_timezone("Timezone (e.g.,US/Eastern, Europe/London,UTC): ")
        return {
            "lat": lat,
            "lon": lon,
            "timezone": tz,
            "city": "Custom Location",
            "country": "",
        }
