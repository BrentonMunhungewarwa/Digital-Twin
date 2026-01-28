import requests
import math
import random
from datetime import datetime, timezone

URL = "https://sacaqm.web.cern.ch/dbwrite.php"

SENSOR_ID = "004B122FD0F8"

def day_fraction():
    now = datetime.now(timezone.utc)
    return (now.hour + now.minute / 60) / 24.0

def sin_cycle(phase_shift=0.0):
    return math.sin(2 * math.pi * (day_fraction() - phase_shift))

def send_data4():
    cycle = sin_cycle(phase_shift=0.25)  # peak mid-afternoon

    temp = 20 + 5 * cycle + random.uniform(-0.3, 0.3)
    humi = 50 - 10 * cycle + random.uniform(-1, 1)
    co2  = 430 - 100 * cycle + random.uniform(-30, 30)

    pm_base = 4 + 10 * max(cycle, 0)
    pm1p0  = pm_base + random.uniform(-2, 2)
    pm2p5  = pm1p0 + 1
    pm4p0  = pm1p0 + 0
    pm10p0 = pm1p0 + 2

    voc = 5 + 2 * max(cycle, 0) + random.uniform(-0.3, 0.3)
    nox = 2 + 3 * max(cycle, 0) + random.uniform(-0.2, 0.2)

    params = {
        "cmd": "add_sen55",
        "sensor_id": "80F3DA537F5C",
        "area": "wifi",
        "operator": "wifi",
        "cellid": "wifi",
        "temp": round(temp, 2),
        "humi": round(humi, 2),
        "pm1p0": round(pm1p0, 2),
        "pm2p5": round(pm2p5, 2),
        "pm4p0": round(pm4p0, 2),
        "pm10p0": round(pm10p0, 2),
        "voc": round(voc, 2),
        "nox": round(nox, 2),
        "co2": int(co2)
    }

    r = requests.get(URL, params=params, timeout=10)

def send_data3():
    cycle = sin_cycle(phase_shift=0.25)  # peak mid-afternoon

    temp = 20 + 5 * cycle + random.uniform(-0.3, 0.3)
    humi = 50 - 10 * cycle + random.uniform(-1, 1)
    co2  = 430 - 100 * cycle + random.uniform(-30, 30)

    pm_base = 2 + 10 * max(cycle, 0)
    pm1p0  = pm_base + random.uniform(-2, 2)
    pm2p5  = pm1p0 + 1
    pm4p0  = pm1p0 + 0
    pm10p0 = pm1p0 + 2

    voc = 5 + 2 * max(cycle, 0) + random.uniform(-0.3, 0.3)
    nox = 2 + 3 * max(cycle, 0) + random.uniform(-0.2, 0.2)

    params = {
        "cmd": "add_sen55",
        "sensor_id": "80F3DA558028",
        "area": "wifi",
        "operator": "wifi",
        "cellid": "wifi",
        "temp": round(temp, 2),
        "humi": round(humi, 2),
        "pm1p0": round(pm1p0, 2),
        "pm2p5": round(pm2p5, 2),
        "pm4p0": round(pm4p0, 2),
        "pm10p0": round(pm10p0, 2),
        "voc": round(voc, 2),
        "nox": round(nox, 2),
        "co2": int(co2)
    }

    r = requests.get(URL, params=params, timeout=10)
def send_data2():
    cycle = sin_cycle(phase_shift=0.25)  # peak mid-afternoon

    temp = 20 + 5 * cycle + random.uniform(-0.3, 0.3)
    humi = 50 - 10 * cycle + random.uniform(-1, 1)
    co2  = 430 - 100 * cycle + random.uniform(-30, 30)

    pm_base = 2 + 10 * max(cycle, 0)
    pm1p0  = pm_base + random.uniform(-2, 2)
    pm2p5  = pm1p0 + 1
    pm4p0  = pm1p0 + 0
    pm10p0 = pm1p0 + 2

    voc = 5 + 2 * max(cycle, 0) + random.uniform(-0.3, 0.3)
    nox = 2 + 3 * max(cycle, 0) + random.uniform(-0.2, 0.2)

    params = {
        "cmd": "add_sen55",
        "sensor_id": "1C6920945B00",
        "area": "wifi",
        "operator": "wifi",
        "cellid": "wifi",
        "temp": round(temp, 2),
        "humi": round(humi, 2),
        "pm1p0": round(pm1p0, 2),
        "pm2p5": round(pm2p5, 2),
        "pm4p0": round(pm4p0, 2),
        "pm10p0": round(pm10p0, 2),
        "voc": round(voc, 2),
        "nox": round(nox, 2),
        "co2": int(co2)
    }

    r = requests.get(URL, params=params, timeout=10)

def send_data():
    cycle = sin_cycle(phase_shift=0.25)  # peak mid-afternoon

    temp = 20 + 5 * cycle + random.uniform(-0.3, 0.3)
    humi = 50 - 10 * cycle + random.uniform(-1, 1)
    co2  = 450 - 100 * cycle + random.uniform(-30, 30)

    pm_base = 3 + 10 * max(cycle, 0)
    pm1p0  = pm_base + random.uniform(-2, 2)
    pm2p5  = pm1p0 + 1
    pm4p0  = pm1p0 + 0
    pm10p0 = pm1p0 + 2

    voc = 3 + 2 * max(cycle, 0) + random.uniform(-0.3, 0.3)
    nox = 2 + 1.5 * max(cycle, 0) + random.uniform(-0.2, 0.2)

    params = {
        "cmd": "add_sen55",
        "sensor_id": SENSOR_ID,
        "area": "wifi",
        "operator": "wifi",
        "cellid": "wifi",
        "temp": round(temp, 2),
        "humi": round(humi, 2),
        "pm1p0": round(pm1p0, 2),
        "pm2p5": round(pm2p5, 2),
        "pm4p0": round(pm4p0, 2),
        "pm10p0": round(pm10p0, 2),
        "voc": round(voc, 2),
        "nox": round(nox, 2),
        "co2": int(co2)
    }

    r = requests.get(URL, params=params, timeout=10)

    
    print(datetime.utcnow().isoformat(), r.status_code, params)

if __name__ == "__main__":
    send_data()
    send_data2()
   # send_data3()
    send_data4()
