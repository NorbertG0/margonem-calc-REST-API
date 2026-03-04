from pydantic import BaseModel, Field

class LegendaryBonusInput(BaseModel):
    item_level: int = Field(..., gt=0)

class VeryCritInput(BaseModel):
    crit_chance: float = Field(..., gt=0)
    crit_power: float = Field(..., gt=0)

class HolyTouchInput(BaseModel):
    hp: int = Field(..., gt=0)

class AnguishInput(BaseModel):
    level: int = Field(..., gt=0)
    strength: int = Field(..., gt=0)
    intellect: int = Field(..., gt=0)
    agility: int = Field(..., gt=0)