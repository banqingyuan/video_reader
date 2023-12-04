from typing import Optional, List, Any

from pydantic import BaseModel

from model.second import SecondInfo


class SceneSeries(BaseModel):
    time_series: List[SecondInfo]
    description: str




