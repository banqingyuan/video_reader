from typing import Optional, List

from pydantic import BaseModel


class InfoUnit(BaseModel):
    story_description: str
    image_description: Optional[str] = None
    image_base64: Optional[str] = None


class SecondInfo(BaseModel):
    second: int
    info_unit_lst: List[InfoUnit]

