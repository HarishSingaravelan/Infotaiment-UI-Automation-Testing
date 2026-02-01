import requests
import os
from playwright.sync_api import sync_playwright
from validators.climate_validator import ClimateState

BASE_API = "http://127.0.0.1:8000/api"

def reset_climate():
    requests.post(f"{BASE_API}/climate/update", json={
        "driver_temp": 22,
        "passenger_temp": 22,
        "fan_speed": 3,
        "mode": "AUTO"
    })



def test_climate_workflow():
    reset_climate() 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000")


        page.fill("#driverTemp", "23")
        page.fill("#passengerTemp", "24")
        page.fill("#fanSpeed", "4")
        page.select_option("#climateMode", "AUTO")

        page.click("text=Apply") 

        page.wait_for_timeout(1000)

        response = requests.get(f"{BASE_API}/climate/status")
        data = response.json()

        ClimateState(**data)
        assert data["driver_temp"] == 23
        assert data["fan_speed"] == 4

        browser.close()
