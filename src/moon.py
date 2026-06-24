#moon.py
from datetime import datetime
import pytz
from skyfield.api import wgs84
from .astronomy import degrees_to_compass
from .constants import MIN_ALTITUDE


def calculate_moon_visibility(loc,eph,ts,local_time=None):
    """Calculates the Moon's current position, visibility, and illumination."""

    earth = eph['earth']
    moon = eph['moon']
    sun = eph['sun']
    location = wgs84.latlon(latitude_degrees=loc['lat'],longitude_degrees=loc['lon'])
    observer = earth+location

    tz = pytz.timezone(loc['timezone'])
    if local_time is None:
        local_time = datetime.now(tz)
    t = ts.from_datetime(local_time)

    astrometric = observer.at(t).observe(moon)
    apparent = astrometric.apparent()
    alt, az, dist = apparent.altaz()

    alt_deg = alt.degrees
    az_deg = az.degrees
    dist_au = dist.au
    compass = degrees_to_compass(az_deg)
    illumination = apparent.fraction_illuminated(sun)
    is_visible = alt_deg >= MIN_ALTITUDE

    result = {
        'name':'Moon',
        'alt_deg':alt_deg,
        'az_deg':az_deg,
        'dist_au':dist_au,
        'compass':compass,
        'illumination':illumination,
        'is_visible':is_visible,
    }

    return result
