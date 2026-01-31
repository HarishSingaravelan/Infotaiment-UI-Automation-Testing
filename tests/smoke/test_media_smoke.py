import requests

BASE = "http://127.0.0.1:8000/api"

def test_media_play_pause_smoke():
    r = requests.post(f"{BASE}/media/play_pause")
    assert r.status_code == 200
    assert "is_playing" in r.json()

def test_media_volume_smoke():
    r = requests.post(f"{BASE}/media/volume/30")
    assert r.status_code == 200
    assert r.json()["volume"] == 30
