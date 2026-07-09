"""
Detects the user's location, loads NASA JPL ephemeris data, calculates
which planets (and the Moon) are currently visible, and prints a report.
"""

from skyfield.api import load
import src.display as display
from src.astronomy import calculate_visibility
from src.location import get_location
from src.moon import calculate_moon_visibility


def main():
    """detect location, calculate visibility, print results."""

    # 1. Setup and Location
    display.print_header()
    loc = get_location()
    display.print_location_found(loc)

    # 2. Astronomy Calculations
    try:
        planets = load("de421.bsp")
    except Exception as e:
        print(f"\nError: Could not load ephemeris data ({e}).")
        return

    ts = load.timescale()
    local_time,planet_results = calculate_visibility(loc,planets,ts)
    moon_result = calculate_moon_visibility(loc,planets,ts,local_time)

    # 3. Output to User
    display.print_observer_info(local_time,loc)
    display.print_moon_result(moon_result)
    visible_count = display.print_planet_results(planet_results)
    display.print_summary(visible_count)


if __name__ == "__main__":
    main()
