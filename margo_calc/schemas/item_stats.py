from pydantic import BaseModel, Field

class EvadeStatsInput(BaseModel):
    evade: int = Field(..., gt=0)
    enemy_level: int = Field(..., gt=1)

class BlockStatsInput(BaseModel):
    block: int = Field(..., gt=0)
    enemy_level: int = Field(..., gt=1)

class ItemPowerStatsInput(BaseModel):
    level: int = Field(..., gt=1)
    rarity_factor: int = Field(..., ge=0, lt=5)

class WeaponDamageStatsInput(BaseModel):
    weapon_factor: float = Field(..., gt=0)
    item_rarity_power: float = Field(..., gt=0)
    item_level_power: float = Field(..., gt=0)
    item_damage_spread: float = Field(..., gt=0)

class WeaponSlowStatsInput(BaseModel):
    slow_factor: float = Field(..., gt=0)
    item_level: int = Field(..., gt=0)

class ArmorPhysicalDamageReductionStatsInput(BaseModel):
    damage_in: int = Field(..., gt=0)
    armor: int = Field(..., gt=0)

class ArmorRangeDamageReductionStatsInput(BaseModel):
    damage_in: int = Field(..., gt=0)
    armor: int = Field(..., gt=0)

class ArmorSecondaryDamageReductionStatsInput(BaseModel):
    damage_in: int = Field(..., gt=0)
    armor: int = Field(..., gt=0)

class ArmorFireDamageReductionStatsInput(BaseModel):
    damage_in: int = Field(..., gt=0)
    armor: int = Field(..., gt=0)

class ArmorFrostDamageReductionStatsInput(BaseModel):
    damage_in: int = Field(..., gt=0)
    armor: int = Field(..., gt=0)

class ArmorLightDamageReductionStatsInput(BaseModel):
    damage_in: int = Field(..., gt=0)
    armor: int = Field(..., gt=0)

class CritChanceGainStatsInput(BaseModel):
    player_level: int = Field(..., gt=0)
    enemy_level: int = Field(..., gt=0)

class CritPowerGainStatsInput(BaseModel):
    player_level: int = Field(..., gt=0)
    enemy_level: int = Field(..., gt=0)

class ItemArmorStatsInput(BaseModel):
    armor_factor: float = Field(..., gt=0)
    class_power: float = Field(..., gt=0)
    rarity_power: float = Field(..., gt=0)
    level_power: float = Field(..., gt=0)

class ItemStatsInput(BaseModel):
    level: int = Field(..., gt=0)
    level_power: Optional[float] = Field(None, gt=0)
    class_power: Optional[float] = Field(None, gt=0)
