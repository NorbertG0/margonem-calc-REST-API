
from fastapi import APIRouter, HTTPException
from core.config import VERSION, ITEMS_TAG
from core.data_loader import ALL_JSON_DATA
from loguru import logger

from services import item_power as item_power_service
from services import armor_damage_reduction as damage_types_service
from services import hero_level as hero_level_service
from services import item_defense as item_defense_service
from services import item_stats as item_stats_service

from schemas.common import *
from schemas.item_stats import *


item_stats_router = APIRouter(prefix=f'/api/{VERSION}/item-stats')

@item_stats_router.post('/item-power', tags=[ITEMS_TAG], response_model=ItemPowerStatsResult)
def calculate_item_power(data: ItemPowerStatsInput):
    logger.info(f'/item-power - Calculating item power with input: {data.model_dump()}')
    item_level_power = item_power_service.calculate_item_level_power(data.level)
    item_rarity_power = item_power_service.calculate_item_rarity_power(data.level, data.rarity_factor)

    result = {
        'item_level_power': item_level_power,
        'item_rarity_power': item_rarity_power
    }

    logger.info(f'/item-power - Item power for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/weapon-damage', tags=[ITEMS_TAG], response_model=WeaponDamageStatsResult)
def calculate_weapon_damage(data: WeaponDamageStatsInput):
    logger.info(f'/weapon-damage - Calculating weapon damage with input: {data.model_dump()}')
    item_damage = item_power_service.calculate_weapon_damage(data.weapon_factor, data.item_rarity_power, data.item_level_power)
    item_damage_top = item_damage  + item_damage * data.item_damage_spread
    item_damage_bottom = item_damage - item_damage * data.item_damage_spread

    result = {
        'item_damage': item_damage,
        'item_damage_top': item_damage_top,
        'item_damage_bottom': item_damage_bottom
    }

    logger.info(f'/weapon-damage - Weapon damage for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/weapon-slow', tags=[ITEMS_TAG], response_model=WeaponSlowStatsResult)
def calculate_weapon_slow(data: WeaponSlowStatsInput):
    logger.info(f'/weapon-slow - Calculating weapon slow with input {data.model_dump()}')
    item_slow = item_power_service.calculate_weapon_slow(data.slow_factor, data.item_level)

    result = {'item_slow': item_slow}

    logger.info(f'/weapon-slow - Weapon slow for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/physical-damage-reduction', tags=[ITEMS_TAG], response_model=ArmorPhysicalDamageReductionStatsResult)
def calculate_physical_damage_reduction(data: ArmorPhysicalDamageReductionStatsInput):
    logger.info(f'/physical-damage-reduction - Calculating physical damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_physical_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/physical-damage-reduction - Physical damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/range-damage-reduction', tags=[ITEMS_TAG], response_model=ArmorRangeDamageReductionStatsResult)
def calculate_range_damage_reduction(data: ArmorRangeDamageReductionStatsInput):
    logger.info(f'/range-damage-reduction - Calculating range damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_range_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/range-damage-reduction - Range damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/secondary-damage-reduction', tags=[ITEMS_TAG], response_model=ArmorSecondaryDamageReductionStatsResult)
def calculate_second_damage_reduction(data: ArmorSecondaryDamageReductionStatsInput):
    logger.info(f'/secondary-damage-reduction - Calculating second damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_secondary_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/secondary-damage-reduction - Secondary damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/fire-damage-reduction', tags=[ITEMS_TAG], response_model=ArmorFireDamageReductionStatsResult)
def calculate_fire_damage_reduction(data: ArmorFireDamageReductionStatsInput):
    logger.info(f'/fire-damage-reduction - Calculating fire damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_fire_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}
    logger.info(f'/fire-damage-reduction - Fire damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/frost-damage-redution', tags=[ITEMS_TAG], response_model=ArmorFrostDamageReductionStatsResult)
def calculate_frost_damage_reduction(data: ArmorFrostDamageReductionStatsInput):
    logger.info(f'/frost-damage-reduction - Calculating frost damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_frost_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/frost-damage-reduction - Frost damage reduction for {data.model_dump()}: {result}')
    return result
@item_stats_router.post('/light-damage-reduction', tags=[ITEMS_TAG], response_model=ArmorLightDamageReductionStatsResult)
def calculate_light_damage_reduction(data: ArmorLightDamageReductionStatsInput):
    logger.info(f'/light-damage-reduction - Calculating light damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_light_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/light-damage-reduction - Light damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/crit-chance-gain', tags=[ITEMS_TAG], response_model=CritChanceGainStatsResult)
def calculate_crit_chance_gain(data: CritChanceGainStatsInput):
    logger.info(f'/crit-chance-gain - Calculating crit chance gain with input: {data.model_dump()}')
    crit_chance_gain = hero_level_service.calculate_crit_chance_gain(data.player_level, data.enemy_level)

    result = {'crit_chance_gain': crit_chance_gain}

    logger.info(f'/crit-chance-gain - Crit chance gain for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/crit-power-gain', tags=[ITEMS_TAG], response_model=CritPowerGainStatsResult)
def calculate_crit_power_gain(data: CritPowerGainStatsInput):
    logger.info(f'/crit-power - Calculating crit power gain with input: {data.model_dump()}')
    crit_power_gain = hero_level_service.calculate_crit_power_gain(data.player_level, data.enemy_level)

    result = {'crit_power_gain': crit_power_gain}

    logger.info(f'/crit-power - Crit power for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/item-armor', tags=[ITEMS_TAG], response_model=ItemArmorStatsResult)
def calculate_item_armor(data: ItemArmorStatsInput):
    logger.info(f'/item-armor - Calculating item armor: {data.model_dump()}')
    armor = item_defense_service.calculate_item_armor(data.armor_factor, data.class_power, data.rarity_power, data.level_power)

    result = {'armor': armor}

    logger.info(f'/item-armor - Item armor for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/item-stats', tags=[ITEMS_TAG], response_model=ItemStatsResult)
def calculate_item_stats(data: ItemStatsInput):
    logger.info(f'/item-stats - Calculating item stats: {data.model_dump()}')

    result = item_stats_service.calculate_item_stats(data)

    logger.info(f'/item-stats - Item stats for {data.model_dump()}: {result}')
    return result

@item_stats_router.get('/bless-legendary-chance', tags=[ITEMS_TAG])
def bless_legendary_chance():
    key = 'legendary_bless_item_chance'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-rarity-amount', tags=[ITEMS_TAG])
def item_rarity_amount():
    key = 'item_rarity_amount'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-loot-chance', tags=[ITEMS_TAG])
def item_lot_chance():
    key = 'item_loot_chance'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-bonus-amount', tags=[ITEMS_TAG])
def item_bonus_amount():
    key = 'item_bonus_amount'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-class-power', tags=[ITEMS_TAG])
def item_class_power():
    key = 'item_class_power'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/weapon-factor', tags=[ITEMS_TAG])
def weapon_factor():
    key = 'weapon_factor'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/slow-factor', tags=[ITEMS_TAG])
def slow_factor():
    key = 'slow_factor'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-manual-bonuses', tags=[ITEMS_TAG])
def item_manual_bonuses():
    key = 'item_manual_bonuses'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-actions', tags=[ITEMS_TAG])
def item_actions():
    key = 'item_actions'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-upgrade-level-factor', tags=[ITEMS_TAG])
def item_upgrade_level_factor():
    key = 'item_upgrade_level_factor'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]