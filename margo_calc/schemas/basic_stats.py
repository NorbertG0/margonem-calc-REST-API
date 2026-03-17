from pydantic import BaseModel, Field
from typing import Optional

class HeroLevelStatsInput(BaseModel):
    level: int = Field(..., gt=0)

class HeroExpAmountInput(BaseModel):
    level: int = Field(..., gt=0)

class HeroExperienceInput(BaseModel):
    player_level: int = Field(..., gt=0)
    npc_level: int = Field(..., gt=0)

class ExperiencePenaltyInput(BaseModel):
    player_level: int = Field(..., gt=0)
    npc_level: int = Field(..., gt=0)

class HighestLevelInGroupInput(BaseModel):
    server_factor: float
    level_ally_min: int

class StrengthStatsInput(BaseModel):
    strength: int = Field(..., gt=0)
    level: int = Field(..., gt=1)
    armor_level: Optional[int] = Field(None, gt=1)

class IntellectStatsInput(BaseModel):
    intellect: int = Field(..., gt=0)
    level: int = Field(..., gt=1)

class DexterityStatsInput(BaseModel):
    dexterity: int = Field(..., gt=0)




