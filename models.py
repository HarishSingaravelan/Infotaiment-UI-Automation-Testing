from pydantic import BaseModel, Field
from typing import Literal


class ClimateState(BaseModel):
    driver_temp: int = Field(22, ge=16, le=30)
    passenger_temp: int = Field(22, ge=16, le=30)
    fan_speed: int = Field(3, ge=1, le=5)
    mode: Literal["AUTO", "MANUAL", "ECO"] = "AUTO"


class MediaState(BaseModel):
    is_playing: bool = False
    volume: int = Field(10, ge=0, le=100)
    source: Literal["Bluetooth", "Radio", "USB"] = "Radio"


class NavigationState(BaseModel):
    destination: str | None = None
    eta_minutes: int | None = None
    is_navigating: bool = False


class SettingsState(BaseModel):
    dark_mode: bool = False
    connectivity: Literal["WiFi", "LTE", "Offline"] = "LTE"
