#astronomy.py
from datetime import datetime
import pytz
from skyfield.api import wgs84
from .constants import MIN_ALTITUDE

def degrees_to_compass(degrees):
    normalized = degrees%360
    directions = ["N","NE","E","SE","S","SW","W","NW"]
    index = int((normalized+22.5)/45)%8
    return directions[index]


def calculate_visibility(loc,planets,ts):
    """Calculates planetary positions and returns the current time and a list of results"""
    earth = planets["earth"]
    location = wgs84.latlon(latitude_degrees=loc["lat"],longitude_degrees=loc["lon"])
    observer = earth + location

    tz = pytz.timezone(loc["timezone"])
    local_time = datetime.now(tz)
    t = ts.from_datetime(local_time)

    targets = {
        "Mercury":planets["mercury"],
        "Venus":planets["venus"],
        "Mars":planets["mars"],
        "Jupiter":planets["jupiter barycenter"],
        "Saturn":planets["saturn barycenter"],
        "Uranus":planets["uranus barycenter"],
        "Neptune":planets["neptune barycenter"]
    }

    results = []
    for name,body in targets.items():
        astrometric = observer.at(t).observe(body)
        alt,az,dist = astrometric.apparent().altaz()

        alt_deg = alt.degrees
        az_deg = az.degrees
        dist_au = dist.au
        compass = degrees_to_compass(az_deg)
        
        is_visible = alt_deg>=MIN_ALTITUDE

        results.append({
            "name":name,
            "alt_deg":alt_deg,
            "az_deg":az_deg,
            "dist_au":dist_au,
            "compass":compass,
            "is_visible":is_visible
        })

    return local_time,results
