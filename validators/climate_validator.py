from pydantic import BaseModel, Field
from typing import Literal


class ClimateState(BaseModel):
    driver_temp: int = Field(ge=16, le=30)
    passenger_temp: int = Field(ge=16, le=30)
    fan_speed: int = Field(ge=1, le=5)
    mode: Literal["AUTO", "MANUAL", "ECO"]
