from pydantic import BaseModel, Field
from typing import Literal


class MediaState(BaseModel):
    is_playing: bool
    volume: int = Field(ge=0, le=100)
    source: Literal["Bluetooth", "Radio", "USB"]
