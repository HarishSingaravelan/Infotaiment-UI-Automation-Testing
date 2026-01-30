import requests
from playwright.sync_api import sync_playwright
from validators.media_validator import MediaState

BASE_API = "http://127.0.0.1:8000/api"


def test_media_volume_change():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("file://" + __import__("os").path.abspath("index.html"))

        page.fill("#volume", "55")
        page.click("text=Set Volume")

        response = requests.get(f"{BASE_API}/media/status")
        data = response.json()

        MediaState(**data)

        browser.close()
