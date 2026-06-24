#main.py
from src.location import get_location
from src.astronomy import calculate_visibility
from src.moon import calculate_moon_visibility
import src.display as display
from skyfield.api import load

def main():


    # 1. Setup and Location
    display.print_header()
    loc = get_location()
    display.print_location_found(loc)

    # 2. Astronomy Calculations
    planets = load("de421.bsp")
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
