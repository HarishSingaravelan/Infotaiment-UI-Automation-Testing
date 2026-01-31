import requests

BASE = "http://127.0.0.1:8000/api"

def test_navigation_eta_generated():
    r = requests.post(f"{BASE}/navigation/set_destination?destination=Office")
    data = r.json()
    assert 5 <= data["eta_minutes"] <= 60

def test_navigation_stop():
    requests.post(f"{BASE}/navigation/set_destination?destination=Mall")
    r = requests.post(f"{BASE}/navigation/stop")
    data = r.json()
    assert data["is_navigating"] is False
    assert data["eta_minutes"] is None
