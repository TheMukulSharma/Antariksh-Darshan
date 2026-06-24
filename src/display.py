# display.py
from .constants import KM_PER_AU, MIN_ALTITUDE

def print_header():
    print("\nANTARIKSH DARSHAN")
    print("="*50)
    print("Detecting your location...")

def print_location_found(loc):
    location_str = f"{loc['city']},{loc['country']}".strip(", ")
    print(f"Found: {location_str}")
    print("Loading NASA JPL planet data...")

def print_observer_info(local_time,loc):
    location_str = f"{loc['city']}, {loc['country']}".strip(", ")
    print("\n"+"="*50)
    print(f"{local_time.strftime('%A %B %d, %Y — %I:%M %p %Z')}")
    print(location_str)
    print(f"{loc['lat']}°,{loc['lon']}°")
    print("="*50)

def print_moon_result(moon):
    print("\nMoon")
    if moon["is_visible"]:
        print(f"Altitude :{moon['alt_deg']:>6.1f}°  above horizon")
        print(f"Direction:{moon['az_deg']:>6.1f}°  ({moon['compass']})")
        print(f"Distance :{moon['dist_au']:.3f} AU  ({moon['dist_au']*KM_PER_AU:.0f} km)")
        print(f"Illumination: {moon['illumination']*100:5.1f}%")
    else:
        if moon["alt_deg"]<0:
            label = "below horizon"
        else:
            label = f"too low ({moon['alt_deg']:.1f}°)"
        print(f"Moon—{label}")
        print(f"Illumination: {moon['illumination']*100:5.1f}%")

def print_planet_results(results):
    visible_count = 0
    for planet in results:
        if planet["is_visible"]:
            visible_count += 1
            print(f"\n{planet['name']}")
            print(f"Altitude :{planet['alt_deg']:>6.1f}°  above horizon")
            print(f"Direction:{planet['az_deg']:>6.1f}°  ({planet['compass']})")
            print(f"Distance :{planet['dist_au']:.3f} AU  ({planet['dist_au'] * KM_PER_AU:.0f} km)")
        else:
            if planet["alt_deg"]<0:
                label = "below horizon"
            else:
                label = f"too low ({planet['alt_deg']:.1f}°)"
            print(f"\n{planet['name']}—{label}")
            
    return visible_count

def print_summary(visible_count):
    print("\n"+"="*50)
    print(f"{visible_count} planet(s) visible right now.")
    print("="*50+"\n")
