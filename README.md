#  Antariksh Darshan

A Python CLI tool that tells you which Planets and the Moon are visible in the  sky
right now — auto-detects your location, no setup required

---

## Features

- Auto-detects your location via IP — no config, no API key
- Checks all 7 planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune
- Accounts for daylight — a planet above the horizon during the day is
  correctly marked not visible, not just "too low"
- Tracks Moon visibility and real-time phase illumination percentage!
- Shows altitude, compass direction, and distance for each planet
- Falls back to manual input if auto-detection fails
- Displays your local time and timezone


---

## Sample Output

```
ANTARIKSH DARSHAN
==================================================
Detecting your location...
Found: New Delhi,India
Loading NASA JPL planet data...

==================================================
Tuesday July 07, 2026 — 08:44 PM IST
Delhi,India
29°,72°
==================================================

Moon
Moon—below horizon
Illumination:  51.2%

Mercury—below horizon

Venus—below horizon

Mars—below horizon

Jupiter—below horizon

Saturn—below horizon

Uranus—below horizon

Neptune—below horizon

==================================================
0 planet(s) visible right now.
==================================================
```

*(a planet that's geometrically above the horizon but hidden by daylight
will instead print something like `Jupiter—up at 45.0°, but it's daylight`)*

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
| NASA JPL      | Ephemeris data (planet positions)                |

---

## How It Works

1. **Location Detection** — Sends a request to  get your latitude,
   longitude, and timezone from your public IP address
2. **Ephemeris Load** — Downloads NASA's ephemeris file which contains
   pre-calculated planet positions from 1900–2050
3. **Position Calculation** — For each planet, Skyfield calculates the apparent
   altitude and azimuth as seen from your exact location at the current moment
4. **Daylight Check** — The Sun's altitude is calculated the same way. The sky
   only counts as dark enough to see planets once the Sun is at least 6°
   below the horizon (the end of civil twilight)
5. **Visibility Filter** — A planet is marked visible only if *both* hold:
   its altitude is above 10° (below that, atmospheric distortion makes
   observation unreliable), *and* the sky is dark enough per the check above.
   A planet can be high in the sky and still correctly show as not visible
   if the Sun hasn't set far enough yet

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
   └── utils.py
```

## What If Auto-Location Detection Fails?
 
If the IP lookup fails, the script will prompt you to enter your location manually.
 
**Step 1 — Find your coordinates**
 
```
Latitude  → positive = North, negative = South
Longitude → positive = East,  negative = West
```
 
**Step 2 — Find your timezone string**
 
Use the exact string of the timezone
Common ones:
 
```
America/New_York      → US East
America/Los_Angeles   → US West
Europe/London         → UK
Asia/Kolkata          → India
Asia/Tokyo            → Japan
Australia/Sydney      → Australia
```
 
**Step 3 — Adjust the visibility thresholds (optional)**
 
Two constants in `src/constants.py` control what counts as "visible":

- `MIN_ALTITUDE` (default `10.0°`) — how high above the horizon a planet
  must be. Below this, Earth's atmosphere blurs the view.
- `SUN_ALTITUDE_LIMIT` (default `-6.0°`) — how far below the horizon the
  Sun must be before the sky counts as dark enough to see planets against.
  Roughly "end of civil twilight." Lower it (e.g. `-12.0`) to require a
  darker sky, or raise it toward `0.0` to allow results in twilight.

---
 
## What I Learned Building This
 
- Astronomical coordinate systems (altitude & azimuth)
- How ephemeris data works and how NASA calculates planet positions
- Working with scientific Python libraries
- IP geolocation APIs and graceful fallback handling
- Structuring a clean single-file Python CLI project
- The difference between a planet being geometrically above the horizon
  and actually visible — daylight can hide something that's high in the sky
 ---
