import requests

BASE = "http://127.0.0.1:8000/api"

def test_navigation_start_smoke():
    r = requests.post(f"{BASE}/navigation/set_destination?destination=Airport")
    assert r.status_code == 200
    data = r.json()
    assert data["is_navigating"] is True
    assert data["destination"] == "Airport"
