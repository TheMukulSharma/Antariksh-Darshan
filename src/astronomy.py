"""
Given an observer's location and a loaded ephemeris, this module works out
where each of the seven classical planets (Mercury through Neptune) currently
sits in the sky, and whether it is high enough above the horizon to be
considered visible.
"""

from .constants import SUN_ALTITUDE_LIMIT
from .utils import get_altaz_info,get_local_time,get_observer,get_sun_altitude,observe



def calculate_visibility(loc, planets, ts):
    """Calculate current altitude, azimuth, and visibility for all planets.
    """
    observer = get_observer(loc, planets)
    local_time = get_local_time(loc)
    t = ts.from_datetime(local_time)
    sun_alt_deg = get_sun_altitude(observer,t,planets)
    sky_is_dark = sun_alt_deg <= SUN_ALTITUDE_LIMIT
    targets = {
        "Mercury":planets["mercury"],
        "Venus":planets["venus"],
        "Mars":planets["mars"],
        "Jupiter":planets["jupiter barycenter"],
        "Saturn":planets["saturn barycenter"],
        "Uranus":planets["uranus barycenter"],
        "Neptune":planets["neptune barycenter"],
    }

    results = []
    for name, body in targets.items():
        apparent = observe(observer,t,body)
        alt_deg,az_deg,dist_au,compass,alt_ok = get_altaz_info(apparent)
        is_visible = alt_ok and sky_is_dark
        results.append(
            {
                "name": name,
                "alt_deg":alt_deg,
                "az_deg":az_deg,
                "dist_au":dist_au,
                "compass":compass,
                "is_visible":is_visible,
                "alt_ok":alt_ok,
            }
        )

    return local_time, results