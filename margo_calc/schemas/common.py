from pydantic import BaseModel

class HeroLevelStatsResult(BaseModel):
    base_hp: float
    base_crit_value: float

class StrengthStatsResult(BaseModel):
    base_hp_gain: float
    armor_hp_gain: float
    total_hp_gain: float
    crit_value_gain: float

class IntellectStatsResult(BaseModel):
    absorb_limit: float
    crit_value_gain: float

class DexterityStatsResult(BaseModel):
    attack_speed: float
    evade_gain: float

class EvadeStatsResult(BaseModel):
    evade_percentage: float

class BlockStatsResult(BaseModel):
    block_percentage: float

class ItemPowerStatsResult(BaseModel):
    item_level_power: float
    item_rarity_power: float

class WeaponDamageStatsResult(BaseModel):
    item_damage: float
    item_damage_top: float
    item_damage_bottom: float

class WeaponSlowStatsResult(BaseModel):
    item_slow: float

class ArmorPhysicalDamageReductionStatsResult(BaseModel):
    damage_out: float

class ArmorRangeDamageReductionStatsResult(BaseModel):
    damage_out: float

class ArmorSecondaryDamageReductionStatsResult(BaseModel):
    damage_out: float

class ArmorFireDamageReductionStatsResult(BaseModel):
    damage_out: float

class ArmorFrostDamageReductionStatsResult(BaseModel):
    damage_out: float

class ArmorLightDamageReductionStatsResult(BaseModel):
    damage_out: float

class CritChanceGainStatsResult(BaseModel):
    crit_chance_gain: int

class CritPowerGainStatsResult(BaseModel):
    crit_power_gain: float

class ItemArmorStatsResult(BaseModel):
    armor: float

class ItemStatsResult(BaseModel):
    all_stats: list[float]
    strength: list[float]
    dexterity: list[float]
    intellect: list[float]
    attack_speed: list[float]
    health_points: list[float]
    heal: list[float]
    armor: list[float]
    poison_resistance: list[float]
    block: list[float]
    evade: list[float]
    weapon_armor_destruction: list[float]
    armor_destruction: list[float]
    resistance_destruction: list[float]
    absorption: list[float]
    magic_absorption: list[float]
    mana: list[float]
    energy: list[float]
    attack_speed_reduction: list[float]
    crit: list[float]
    physical_crit_power: list[float]
    magic_crit_power: list[float]
    crit_chance_reduction: list[float]
    energy_reduction_chance: list[float]
    energy_reduction_value: float
    mana_reduction_chance: list[float]
    mana_reduction_value: float
    evade_reduction: list[float]
    fire_resists: list[float]
    frost_resists: list[float]
    light_resists: list[float]

class LegendaryBonusResult(BaseModel):
    first_nerf_level: float
    expiration_level: float

class VeryCritResult(BaseModel):
    very_crit_chance: float
    very_crit_power: float

class HolyTouchResult(BaseModel):
    healing_per_round: float
    rounds: int
    total_healing: float

class AnguishResult(BaseModel):
    damage: float