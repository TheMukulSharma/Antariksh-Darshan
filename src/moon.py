"""Moon visibility and illumination calculations."""

from .utils import get_altaz_info, get_local_time, get_observer, observe


def calculate_moon_visibility(loc, eph, ts, local_time=None):
    """Calculate the Moon's current position, visibility, and illumination."""
    try:
        observer = get_observer(loc, eph)
        local_time = get_local_time(loc, local_time)
        t = ts.from_datetime(local_time)

        moon = eph["moon"]
        sun = eph["sun"]

        apparent = observe(observer, t, moon)
        alt_deg, az_deg, dist_au, compass, is_visible = get_altaz_info(apparent)
        illumination = apparent.fraction_illuminated(sun)

        return {
            "name": "Moon",
            "alt_deg": alt_deg,
            "az_deg": az_deg,
            "dist_au": dist_au,
            "compass": compass,
            "illumination": illumination,
            "is_visible": is_visible,
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
