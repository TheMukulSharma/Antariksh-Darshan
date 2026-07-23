from .constants import KM_PER_AU


def print_header():
    """Print the app banner shown at startup."""
    print("\n+------------------------------------------------+")
    print("|               ANTARIKSH DARSHAN                |")
    print("+------------------------------------------------+")
    print("Detecting your location...")


def print_row(text):
    print("|" + text.center(48) + "|")


def print_location_found(loc):
    """Print the detected (or manually entered) location."""
    location_str = f"{loc['city']},{loc['country']}".strip(", ")
    print(f"Found: {location_str}")
    print("Loading NASA JPL planet data...\n")


def print_observer_info(local_time, loc):
    """Print the observation timestamp and location header"""
    location_str = f"{loc['city']},{loc['country']}".strip(", ")
    print("+" + "-" * 48 + "+")
    print_row(f"{local_time.strftime('%A %B %d, %Y — %I:%M %p %Z')}")
    print_row(location_str)
    print_row(f"{loc['lat']}°,{loc['lon']}°")
    print("+" + "-" * 48 + "+")


def print_moon_result(moon):
    """Print the Moon's altitude, direction, distance, and illumination."""
    if moon is None:
        print("\nMOON [DATA UNAVAILABLE]")
        return

    if moon["is_visible"]:
        print("\nMOON [VISIBLE]")
        print(f"   |-- Altitude : {moon['alt_deg']:>6.1f}° above horizon")
        print(f"   |-- Direction: {moon['az_deg']:>6.1f}° ({moon['compass']})")
        print(
            f"   |-- Distance : {moon['dist_au']:.3f} AU ({moon['dist_au']*KM_PER_AU:,.0f} km)"
        )
        print(f"   |-- Phase    : {moon['illumination']*100:.1f}% Illumination")
    else:
        if moon["alt_deg"] < 0:
            label = "Below Horizon"
        elif not moon["alt_ok"]:
            label = f"Too Low ({moon['alt_deg']:.1f}°)"
        else:
            label = f"Up at {moon['alt_deg']:.1f}°, but it's daylight"

        print(f"\nMOON [{label.upper()}]")
        print(f"   |-- Phase    : {moon['illumination'] * 100:.1f}% Illumination")


def print_planet_results(results):
    """Print each planet's visibility and return how many are visible."""
    visible = 0
    for planet in results:
        Name = planet["name"].upper()
        if planet["is_visible"]:
            visible += 1
            print(f"\n{Name} [VISIBLE]")
            print(f"   |-- Altitude : {planet['alt_deg']:>6.1f}° above horizon")
            print(f"   |-- Direction: {planet['az_deg']:>6.1f}° ({planet['compass']})")
            print(
                f"   |-- Distance : {planet['dist_au']:.3f} AU ({planet['dist_au']*KM_PER_AU:,.0f} km)"
            )
        else:
            if planet["alt_deg"] < 0:
                label = "Below Horizon"
            elif not planet["alt_ok"]:
                label = f"Too Low ({planet['alt_deg']:.1f}°)"
            else:
                label = f"Up at {planet['alt_deg']:.1f}°, but it's daylight"
            print(f"\n{Name} [{label.upper()}]")
    return visible


def print_summary(visible_count):
    """Print the final 'N planets visible' summary card."""
    msg = f"{visible_count} planet(s) visible right now!"
    print("+" + "-" * 48 + "+")
    print_row(msg)
    print("+" + "-" * 48 + "+")
