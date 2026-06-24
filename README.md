#  Antariksh Darshan

A Python CLI tool that tells you which planets are visible in the night sky
right now — auto-detects your location, no setup required
---

## Features

- Auto-detects your location via IP — no config, no API key
- Checks all 7 planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune
- Tracks Moon visibility and real-time phase illumination percentage!
- Shows altitude, compass direction, and distance for each planet
- Falls back to manual input if auto-detection fails
- Displays your local time and timezone

---

## Sample Output

```
========================================
Antariksh Darshan
========================================
Detecting your location...
Found: India 
Loading NASA JPL planet data...

========================================
Tuesday June 09,2026 — 09:10 PM IST
Delhi, India
28.6°, 77.2°
========================================

Moon
Altitude :  42.5°  above horizon
Direction: 184.2°  (S)
Distance : 0.00263 AU  (393441 km)
Illumination:  34.2%

Mercury — below horizon

Venus — too low (8.9°)

Mars — below horizon

Jupiter — too low (8.0°)

Saturn — below horizon

Uranus — below horizon

Neptune — below horizon

========================================
 0 planet(s) visible right now.
========================================
```

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/TheMukulSharma/Antariksh-Darshan.git

# 2. Navigate into the folder
cd Antariksh-Darshan

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run it
python main.py
```

> **Note:** On first run, Skyfield downloads `de421.bsp` (~17MB) from NASA JPL.
> This is a one-time download and is cached locally for all future runs.

---

## Tech Stack
 
| Tool          | Purpose                                          |
|---------------|--------------------------------------------------|
| Python 3      | Core language                                    |
| Skyfield      | Astronomical calculations using NASA JPL data    |
| requests      | HTTP calls for IP geolocation                    |
| pytz          | Timezone handling                                |
| NASA JPL DE421| Ephemeris data (planet positions)                |

---

## How It Works

1. **Location Detection** — Sends a request to  get your latitude,
   longitude, and timezone from your public IP address
2. **Ephemeris Load** — Downloads NASA's DE421 ephemeris file which contains
   pre-calculated planet positions from 1900–2050
3. **Position Calculation** — For each planet, Skyfield calculates the apparent
   altitude and azimuth as seen from your exact location at the current moment
4. **Visibility Filter** — Any planet with an altitude above 10° is marked visible.
   Below 10°, atmospheric distortion makes observation unreliable

---

## Project Structure

```
Antariksh-Darshan/
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── src/        
   ├── astronomy.py
   ├── constants.py
   ├── display.py
   ├── location.py
   └── moon.py
```

## What If Auto-Location Detection Fails?
 
If the IP lookup fails, the script will prompt you to enter your location manually.
 
**Step 1 — Find your coordinates**
 
Go to [latlong.net](https://www.latlong.net/), type your city, and copy the numbers shown.
 
```
Latitude  → positive = North, negative = South
Longitude → positive = East,  negative = West
```
 
**Step 2 — Find your timezone string**
 
Use the exact string from the [tz database list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Common ones:
 
```
America/New_York      → US East
America/Los_Angeles   → US West
Europe/London         → UK
Asia/Kolkata          → India
Asia/Tokyo            → Japan
Australia/Sydney      → Australia
```
 
**Step 3 — Adjust minimum altitude (optional)**
 
`MIN_ALTITUDE` in `src/constants.py` is set to `10.0` degrees. Below that, Earth's atmosphere
blurs the view. Set it to `0.0` if you want to see everything above the horizon.
 
---
 
## What I Learned Building This
 
- Astronomical coordinate systems (altitude & azimuth)
- How ephemeris data works and how NASA calculates planet positions
- Working with third-party scientific Python libraries
- IP geolocation APIs and graceful fallback handling
- Structuring a clean single-file Python CLI project
---
 

## License
 MIT License


---

## Acknowledgements

- [Skyfield](https://rhodesmill.org/skyfield/)
- [NASA JPL](https://naif.jpl.nasa.gov/)
- [ip-api.com](http://ip-api.com)
