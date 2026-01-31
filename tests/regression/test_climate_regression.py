import requests

BASE = "http://127.0.0.1:8000/api"

def test_climate_temperature_boundaries():
    payload = {"driver_temp": 16, "passenger_temp": 30, "fan_speed": 5, "mode": "ECO"}
    r = requests.post(f"{BASE}/climate/update", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert 16 <= data["driver_temp"] <= 30
    assert data["mode"] == "ECO"

