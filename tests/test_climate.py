import requests
from playwright.sync_api import sync_playwright
from validators.climate_validator import ClimateState

BASE_API = "http://127.0.0.1:8000/api"


def test_climate_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("file://" + __import__("os").path.abspath("index.html"))

        # UI Actions
        page.fill("#driverTemp", "25")
        page.fill("#passengerTemp", "24")
        page.fill("#fanSpeed", "4")
        page.select_option("#climateMode", "AUTO")
        page.click("text=Apply Climate")

        # Fetch backend state
        response = requests.get(f"{BASE_API}/climate/status")
        data = response.json()

        # Validate using Pydantic
        ClimateState(**data)
        browser.close()
