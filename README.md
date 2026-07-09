# Antariksh Darshan

A Python CLI tool that tells you which planets and the Moon are visible in the night sky right now — auto-detects your location with zero setup required.

---

## Features

- **Auto-Location Detection** — Uses your IP address to find your location (no API keys or configuration needed).
- **Comprehensive Tracking** — Checks all 7 major planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune.
- **Moon Phase Analytics** — Tracks real-time Moon visibility and illumination percentage.
- **Detailed Metrics** — Provides altitude, compass direction (azimuth), and distance for every celestial body.
- **Smart Fallback** — Prompts for manual coordinate input if auto-detection fails.
- **Localized Time** — Automatically adapts to your local time and timezone.

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
*(Actual values depend on your real location and time.)*

---

## Project structure

```
Antariksh-Darshan/
├── main.py   
├── src/
│   ├── location.py
│   ├── astronomy.py
│   ├── moon.py    
│   ├── utils.py   
│   ├── display.py     
│   └── constants.py   
├── requirements.txt
└── LICENSE

```

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
2. **Ephemeris Load** — Downloads NASA's  ephemeris file which contains
   pre-calculated planet positions from 1900–2050
3. **Position Calculation** — For each planet, Skyfield calculates the apparent
   altitude and azimuth as seen from your exact location at the current moment
4. **Visibility Filter** — Any planet with an altitude above 10° is marked visible.
   Below 10°, atmospheric distortion makes observation unreliable

 ---
 
## What If Auto-Location Detection Fails?
 
If the IP lookup fails, the script will prompt you to enter your location manually.
 
**Step 1 — Find your coordinates**

**Step 2 — Find your timezone string**
 
Use the exact string of the TIME ZONE
Common ones:
 
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
- Working with  scientific Python libraries
- IP geolocation APIs and graceful fallback handling
- Structuring a clean  Python CLI project
---
