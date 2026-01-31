import requests

BASE = "http://127.0.0.1:8000/api"

def test_media_volume_limits():
    r = requests.post(f"{BASE}/media/volume/150")
    assert r.json()["volume"] == 100

    r = requests.post(f"{BASE}/media/volume/-10")
    assert r.json()["volume"] == 0

def test_media_source_change():
    r = requests.post(f"{BASE}/media/source/FM")
    assert r.status_code == 200
    assert r.json()["source"] == "FM"
