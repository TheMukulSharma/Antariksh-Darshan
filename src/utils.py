"""Shared helpers for astronomical visibility calculations.

Both the planet calculations (``astronomy.py``) and the Moon calculation
(``moon.py``) need to do the same three things: build an observer at the
user's location, resolve what "now" means in the user's timezone, and turn
a Skyfield observation into altitude/azimuth/distance/compass/visibility.
Keeping that logic in one place means both modules stay focused on *what*
they calculate, not *how* the underlying Skyfield calls work.
"""

from datetime import datetime
import pytz
from skyfield.api import wgs84
from .constants import MIN_ALTITUDE


def get_observer(loc, eph):
    """Build a topocentric observer for the given location.
    """
    earth = eph["earth"]
    surface = wgs84.latlon(latitude_degrees=loc["lat"], longitude_degrees=loc["lon"])
    return earth + surface


def get_local_time(loc, local_time=None):
    """Resolve the local datetime to use for an observation.
    """
    if local_time is not None:
        return local_time
    tz = pytz.timezone(loc["timezone"])
    return datetime.now(tz)


def degrees_to_compass(degrees):
    """Convert an azimuth angle into an 8-point compass direction.
    """
    normalized = degrees % 360
    directions = ["N","NE","E","SE","S","SW","W","NW"]
    index = int((normalized+22.5)/45)%8
    return directions[index]


def observe(observer, t, body):
    """Observe a body from an observer at a given time..
    """
    astrometric = observer.at(t).observe(body)
    return astrometric.apparent()


def get_altaz_info(apparent):
    """Extract altitude, azimuth, distance, compass, and visibility.
    """
    alt, az, dist = apparent.altaz()
    alt_deg = alt.degrees
    az_deg = az.degrees
    dist_au = dist.au
    compass = degrees_to_compass(az_deg)
    is_visible = alt_deg >= MIN_ALTITUDE
    return alt_deg, az_deg, dist_au, compass, is_visible
