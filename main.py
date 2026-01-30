# main.py
from fastapi import FastAPI
from models import ClimateState, MediaState, NavigationState, SettingsState
import random

app = FastAPI(title="Mock Tesla Infotainment System")

# In-memory "vehicle state"
climate_state = ClimateState()
media_state = MediaState()
navigation_state = NavigationState()
settings_state = SettingsState()

#--------Climate Control -------------------

@app.get("/api/climate/status", response_model=ClimateState)
def get_climate_status():
    return climate_state


@app.post("/api/climate/update", response_model=ClimateState)
def update_climate(new_state: ClimateState):
    global climate_state
    climate_state = new_state
    return climate_state

# -------Media player--------------------

@app.get("/api/media/status", response_model=MediaState)
def get_media_status():
    return media_state


@app.post("/api/media/play_pause", response_model=MediaState)
def toggle_play_pause():
    media_state.is_playing = not media_state.is_playing
    return media_state


@app.post("/api/media/volume/{level}", response_model=MediaState)
def set_volume(level: int):
    media_state.volume = max(0, min(level, 100))
    return media_state


@app.post("/api/media/source/{source}", response_model=MediaState)
def change_source(source: str):
    media_state.source = source
    return media_state


#--------------Navigation---------------
@app.get("/api/navigation/status", response_model=NavigationState)
def get_navigation_status():
    return navigation_state


@app.post("/api/navigation/set_destination", response_model=NavigationState)
def set_destination(destination: str):
    navigation_state.destination = destination
    navigation_state.eta_minutes = random.randint(5, 60)
    navigation_state.is_navigating = True
    return navigation_state


@app.post("/api/navigation/stop", response_model=NavigationState)
def stop_navigation():
    navigation_state.is_navigating = False
    navigation_state.eta_minutes = None
    return navigation_state


#--------Settings-----------------------
@app.get("/api/settings/status", response_model=SettingsState)
def get_settings():
    return settings_state


@app.post("/api/settings/dark_mode/{enabled}", response_model=SettingsState)
def toggle_dark_mode(enabled: bool):
    settings_state.dark_mode = enabled
    return settings_state


@app.post("/api/settings/connectivity/{mode}", response_model=SettingsState)
def set_connectivity(mode: str):
    settings_state.connectivity = mode
    return settings_state

