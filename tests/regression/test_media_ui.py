import requests
import os
from playwright.sync_api import sync_playwright
from validators.media_validator import MediaState

BASE_API = "http://127.0.0.1:8000/api"

def reset_media():
    requests.post(f"{BASE_API}/media/source/Radio")
    requests.post(f"{BASE_API}/media/volume/10")


def test_media_volume_change():
    reset_media()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file://" + os.path.abspath("index.html"))

        page.fill("#volume", "55")
        page.click("text=Set")

        page.wait_for_timeout(1000)

        response = requests.get(f"{BASE_API}/media/status")
        data = response.json()

        MediaState(**data)
        assert data["volume"] == 55

        browser.close()
