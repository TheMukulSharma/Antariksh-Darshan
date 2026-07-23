"""Moon visibility and illumination calculations."""

from .constants import SUN_ALTITUDE_LIMIT
from .utils import (
    get_altaz_info,
    get_local_time,
    get_observer,
    get_sun_altitude,
    observe,
)


def calculate_moon_visibility(loc, eph, ts, local_time=None):
    """Calculate the Moon's current position, visibility, and illumination."""
    try:
        observer = get_observer(loc, eph)
        local_time = get_local_time(loc, local_time)
        t = ts.from_datetime(local_time)

        moon = eph["moon"]
        sun = eph["sun"]

        apparent = observe(observer, t, moon)
        alt_deg, az_deg, dist_au, compass, alt_ok = get_altaz_info(apparent)
        illumination = apparent.fraction_illuminated(sun)

        sun_alt_deg = get_sun_altitude(observer, t, eph)
        sky_is_dark = sun_alt_deg <= SUN_ALTITUDE_LIMIT
        is_visible = alt_ok and sky_is_dark

        return {
            "name": "Moon",
            "alt_deg": alt_deg,
            "az_deg": az_deg,
            "dist_au": dist_au,
            "compass": compass,
            "illumination": illumination,
            "is_visible": is_visible,
            "alt_ok": alt_ok,
        }

    except (ValueError, TypeError) as e:
        print(f"Calculation failed due to invalid input data or time format: {e}")
        return None

    except KeyError as e:
        print(f"Missing key: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
