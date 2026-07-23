"""Moon visibility and illumination calculations."""

from .constants import (
    SUN_ALTITUDE_LIMIT,
    DANJON_LIMIT_DEG,
    DAYLIGHT_MIN_ELONGATION,
)

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
        time = get_local_time(loc, local_time)
        t = ts.from_datetime(time)

        moon = eph["moon"]
        sun = eph["sun"]

        apparent = observe(observer, t, moon)
        sun_apparent = observe(observer, t, sun)

        alt_deg, az_deg, dist_au, compass, alt_ok = get_altaz_info(apparent)

        elongation_deg = apparent.separation_from(sun_apparent).degrees
        illumination = apparent.fraction_illuminated(sun)

        sun_alt_deg = get_sun_altitude(observer, t, eph)
        sky_is_dark = sun_alt_deg <= SUN_ALTITUDE_LIMIT

        # Check : Must be outside the solar glare zone (Danjon limit)
        outside_solar_glare = elongation_deg >= DANJON_LIMIT_DEG

        # Check : Daylight contrast check
        daylight_contrast_ok = sky_is_dark or (
            elongation_deg >= DAYLIGHT_MIN_ELONGATION
        )

        is_visible = alt_ok and outside_solar_glare and daylight_contrast_ok

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

    except (ValueError, TypeError, KeyError) as e:
        print(f"Data or key error during calculation: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
