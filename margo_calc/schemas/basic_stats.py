from pydantic import BaseModel, Field
from typing import Optional

class HeroLevelStatsInput(BaseModel):
    level: int = Field(..., gt=0)

class StrengthStatsInput(BaseModel):
    strength: int = Field(..., gt=0)
    level: int = Field(..., gt=1)
    armor_level: Optional[int] = Field(None, gt=1)

class IntellectStatsInput(BaseModel):
    intellect: int = Field(..., gt=0)
    level: int = Field(..., gt=1)

class DexterityStatsInput(BaseModel):
    dexterity: int = Field(..., gt=0)




