import requests

BASE = "http://127.0.0.1:8000/api"

def test_dark_mode_toggle():
    r = requests.post(f"{BASE}/settings/dark_mode/true")
    assert r.json()["dark_mode"] is True

    r = requests.post(f"{BASE}/settings/dark_mode/false")
    assert r.json()["dark_mode"] is False

def test_connectivity_modes():
    r = requests.post(f"{BASE}/settings/connectivity/WIFI")
    assert r.json()["connectivity"] == "WIFI"
