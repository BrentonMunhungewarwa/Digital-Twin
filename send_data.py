import requests
import math
import random
import time
from datetime import datetime, timezone

URL = "https://sacaqm.web.cern.ch/dbwrite.php"

# --- persistent drift state ---
sensor_state = {}

def day_fraction():
    now = datetime.now(timezone.utc)
    return (now.hour + now.minute / 60) / 24.0

def daily_cycle():
    return math.sin(2 * math.pi * (day_fraction() - 0.25))

def is_work_hours():
    now = datetime.now(timezone.utc)
    return 8 <= now.hour <= 18

def get_state(sensor_id):
    if sensor_id not in sensor_state:
        sensor_state[sensor_id] = {
            "temp": 20 + random.uniform(-1, 1),
            "co2": 420 + random.uniform(-20, 20),
            "pm": 5 + random.uniform(0, 5)
        }
    return sensor_state[sensor_id]

def simulate_sensor(sensor_id, profile):

    state = get_state(sensor_id)
    cycle = daily_cycle()
    work = is_work_hours()

    # --- slow drift (random walk) ---
    state["temp"] += random.uniform(-0.05, 0.05)
    state["co2"]  += random.uniform(-5, 5)
    state["pm"]   += random.uniform(-0.2, 0.2)

    # --- base values ---
    temp = state["temp"] + 3 * cycle
    humi = 50 - 8 * cycle + random.uniform(-2, 2)

    # --- occupancy effect ---
    if work:
        co2 = state["co2"] + random.uniform(50, 200)
        voc = 4 + random.uniform(1, 3)
    else:
        co2 = state["co2"]
        voc = 2 + random.uniform(-0.5, 0.5)

    # --- random pollution event ---
    if random.random() < 0.05:  # 5% chance spike
        spike = random.uniform(10, 40)
        state["pm"] += spike
        print("PM EVENT on", sensor_id)

    pm1 = max(1, state["pm"])
    pm2 = pm1 + random.uniform(0.5, 1.5)
    pm4 = pm1 + random.uniform(1, 3)
    pm10 = pm1 + random.uniform(2, 5)

    nox = 1 + (2 if work else 0) + random.uniform(-0.3, 0.3)

    params = {
        "cmd": "add_sen55",
        "sensor_id": sensor_id,
        "area": profile,
        "operator": "wifi",
        "cellid": "wifi",
        "temp": round(temp, 2),
        "humi": round(humi, 2),
        "pm1p0": round(pm1, 2),
        "pm2p5": round(pm2, 2),
        "pm4p0": round(pm4, 2),
        "pm10p0": round(pm10, 2),
        "voc": round(voc, 2),
        "nox": round(nox, 2),
        "co2": int(co2)
    }

    try:
        r = requests.get(URL, params=params, timeout=10)
        print(datetime.utcnow().isoformat(), sensor_id, r.status_code)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":

    sensors = {
        "004B122FD0F8": "office",
        "1C6920945B00": "lab",
        "80F3DA558028": "corridor",
        "80F3DA537F5C": "meeting_room",
        "80F3DA5544D4": "storage",
        "80F3DA558250": "entrance"
    }

    for sid, profile in sensors.items():
        simulate_sensor(sid, profile)
