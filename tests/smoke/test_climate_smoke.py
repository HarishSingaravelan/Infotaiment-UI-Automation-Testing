import requests

BASE = "http://127.0.0.1:8000/api"

def test_climate_update_smoke():
    payload = {
        "driver_temp": 24,
        "passenger_temp": 23,
        "fan_speed": 3,
        "mode": "AUTO"
    }

    r = requests.post(f"{BASE}/climate/update", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert data["driver_temp"] == 24
    assert data["mode"] == "AUTO"
