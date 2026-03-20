import json
from pathlib import Path

from fastapi import APIRouter, Request, HTTPException
from loguru import logger
from datetime import datetime

from schemas.basic_stats import *
from schemas.common import *
from schemas.legendary_bonuses import *
from schemas.item_stats import *
from services import strength as strength_service
from services import intellect as intellect_service
from services import dexterity as dexterity_service
from services import evade as evade_service
from services import block as block_service
from services import item_power as item_power_service
from services import armor_damage_reduction as damage_types_service
from services import hero_level as hero_level_service
from services import item_defense as item_defense_service
from services import item_stats as item_stats_service
from services import legendary_bonuses as legendary_bonus_service

from additional_functions import calculate_range

RANGE_NEG2_5 = range(-2, 6)
RANGE_0_5 = range(0, 6)

version = 'v1'
router = APIRouter(prefix=f'/api/{version}')
hero_stats_router = APIRouter(prefix=f'/api/{version}/hero-stats')
item_stats_router = APIRouter(prefix=f'/api/{version}/item-stats')
legendary_bonus_router = APIRouter(prefix=f'/api/{version}/legendary-bonus')
config_router = APIRouter(prefix=f'/api/{version}/config')

config_tag = 'Config'
stats_tag = 'Hero stats'
item_tag = 'Items stats'
legendary_bonus_tag = 'Legendary bonuses'

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

ALL_JSON_DATA = {}
for file_path in DATA_DIR.glob("*.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        key = file_path.stem
        ALL_JSON_DATA[key] = json.load(f)

@config_router.get('/health', tags=[config_tag])
def health():
    logger.info('/health - Health check')
    return {'status': 'ok'}

@hero_stats_router.post('/base-stats', tags=[stats_tag], response_model=HeroLevelStatsResult)
def calculate_base_hp(data: HeroLevelStatsInput):
    logger.info(f'/base-stats - Calculating base stats with input: {data.model_dump()}')
    base_hp = hero_level_service.calculate_base_hp(data.level)
    base_crit_value =  hero_level_service.calculate_base_crit_value(data.level)

    result = {
        'base_hp': base_hp,
        'base_crit_value': base_crit_value
    }

    logger.info(f'/base-stats - Base stats for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/exp-amount', tags=[stats_tag], response_model=HeroExpAmountResult)
def calculate_exp_amount(data: HeroExpAmountInput):
    logger.info(f'/exp-amount - Calculating exp amount with input: {data.model_dump()}')
    exp_amount = hero_level_service.calculate_exp_amount(data.level)

    result = {'exp_amount': exp_amount}

    logger.info(f'/exp-amount - Exp amount for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/experience', tags=[stats_tag], response_model=HeroExperienceResult)
def calculate_experience(data: HeroExperienceInput):
    logger.info(f'/experience - Calculating experience with input: {data.model_dump()}')
    experience = hero_level_service.calculate_experience(data.player_level, data.npc_level)

    result = {'experience': experience}

    logger.info(f'/experience - Experience for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/experience-penalty', tags=[stats_tag], response_model=ExperiencePenaltyResult)
def calculate_experience_penalty(data: ExperiencePenaltyInput):
    logger.info(f'/experience-penalty - Calculating experience penalty with input: {data.model_dump()}')
    experience_penalty = hero_level_service.calculate_experience_penalty(data.player_level, data.npc_level)

    result = {'experience_penalty': experience_penalty}

    logger.info(f'/experience-penalty - Experience penalty for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/highest-level', tags=[stats_tag], response_model=HighestLevelInGroupResult)
def calculate_highest_level_in_group(data: HighestLevelInGroupInput):
    logger.info(f'/highest-level - Calculating highest level in group with input: {data.model_dump()}')
    max_level = hero_level_service.calculate_highest_level_in_group(data.server_factor, data.level_ally_min)

    result = {'max_level': max_level}

    logger.info(f'/highest-level - Highest level in group {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/strength', tags=[stats_tag], response_model=StrengthStatsResult)
def calculate_strength_stats(data: StrengthStatsInput):
    logger.info(f'/strength - Calculating strength stats with input: {data.model_dump()}')
    base_hp = strength_service.calculate_base_hp(data.strength)
    armor_hp = strength_service.calculate_armor_hp(data.strength, data.armor_level)
    crit_gain = strength_service.calculate_crit_value(data.strength, data.level)
    total_hp_gain = base_hp + armor_hp

    result = {
        'base_hp_gain': base_hp,
        'armor_hp_gain': armor_hp,
        'total_hp_gain': total_hp_gain,
        'crit_value_gain': crit_gain
    }

    logger.info(f'/strength - Strength stats for {data.model_dump()}: {result}')

    return result

@hero_stats_router.post('/intellect', tags=[stats_tag], response_model=IntellectStatsResult)
def calculate_intellect_stats(data: IntellectStatsInput):
    logger.info(f'/intellect - Calculating intellect stats with input: {data.model_dump()}')
    absorb_limit = intellect_service.calculate_absorb_limit(data.intellect)
    crit_gain = intellect_service.calculate_crit_value(data.intellect, data.level)

    result = {
        'absorb_limit': absorb_limit,
        'crit_value_gain': crit_gain
    }

    logger.info(f'/intellect - Intellect stats for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/dexterity', tags=[stats_tag], response_model=DexterityStatsResult)
def calculate_dexterity_stats(data: DexterityStatsInput):
    logger.info(f'/dexterity - Calculating dexterity stats with input: {data.model_dump()}')
    attack_speed = dexterity_service.calculate_attack_speed(data.dexterity)
    evade_gain = dexterity_service.calculate_evade_gain(data.dexterity)

    result = {
        'attack_speed': attack_speed,
        'evade_gain': evade_gain,
    }

    logger.info(f'/dexterity - Dexterity stats for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/evade', tags=[stats_tag], response_model=EvadeStatsResult)
def calculate_evade_percentage(data: EvadeStatsInput):
    logger.info(f'/evade - Calculating evade percentage with input: {data.model_dump()}')
    evade_percentage = evade_service.calculate_evade(data.evade, data.enemy_level)

    result = {'evade_percentage': evade_percentage}

    logger.info(f'/evade - Evade percentage for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/block', tags=[stats_tag], response_model=BlockStatsResult)
def calculate_block_percentage(data: BlockStatsInput):
    logger.info(f'/block - Calculating block percentage with input: {data.model_dump()}')
    block_percentage = block_service.calculate_block(data.block, data.enemy_level)

    result = {'block_percentage': block_percentage}

    logger.info(f'/block - Block percentage for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/item-power', tags=[item_tag], response_model=ItemPowerStatsResult)
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

@item_stats_router.post('/weapon-damage', tags=[item_tag], response_model=WeaponDamageStatsResult)
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

@item_stats_router.post('/weapon-slow', tags=[item_tag], response_model=WeaponSlowStatsResult)
def calculate_weapon_slow(data: WeaponSlowStatsInput):
    logger.info(f'/weapon-slow - Calculating weapon slow with input {data.model_dump()}')
    item_slow = item_power_service.calculate_weapon_slow(data.slow_factor, data.item_level)

    result = {'item_slow': item_slow}

    logger.info(f'/weapon-slow - Weapon slow for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/physical-damage-reduction', tags=[item_tag], response_model=ArmorPhysicalDamageReductionStatsResult)
def calculate_physical_damage_reduction(data: ArmorPhysicalDamageReductionStatsInput):
    logger.info(f'/physical-damage-reduction - Calculating physical damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_physical_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/physical-damage-reduction - Physical damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/range-damage-reduction', tags=[item_tag], response_model=ArmorRangeDamageReductionStatsResult)
def calculate_range_damage_reduction(data: ArmorRangeDamageReductionStatsInput):
    logger.info(f'/range-damage-reduction - Calculating range damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_range_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/range-damage-reduction - Range damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/secondary-damage-reduction', tags=[item_tag], response_model=ArmorSecondaryDamageReductionStatsResult)
def calculate_second_damage_reduction(data: ArmorSecondaryDamageReductionStatsInput):
    logger.info(f'/secondary-damage-reduction - Calculating second damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_secondary_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/secondary-damage-reduction - Secondary damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/fire-damage-reduction', tags=[item_tag], response_model=ArmorFireDamageReductionStatsResult)
def calculate_fire_damage_reduction(data: ArmorFireDamageReductionStatsInput):
    logger.info(f'/fire-damage-reduction - Calculating fire damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_fire_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}
    logger.info(f'/fire-damage-reduction - Fire damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/frost-damage-redution', tags=[item_tag], response_model=ArmorFrostDamageReductionStatsResult)
def calculate_frost_damage_reduction(data: ArmorFrostDamageReductionStatsInput):
    logger.info(f'/frost-damage-reduction - Calculating frost damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_frost_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/frost-damage-reduction - Frost damage reduction for {data.model_dump()}: {result}')
    return result
@item_stats_router.post('/light-damage-reduction', tags=[item_tag], response_model=ArmorLightDamageReductionStatsResult)
def calculate_light_damage_reduction(data: ArmorLightDamageReductionStatsInput):
    logger.info(f'/light-damage-reduction - Calculating light damage reduction with input: {data.model_dump()}')
    damage_out = damage_types_service.calculate_light_damage_reduction(data.damage_in, data.armor)

    result = {'damage_out': damage_out}

    logger.info(f'/light-damage-reduction - Light damage reduction for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/crit-chance-gain', tags=[item_tag], response_model=CritChanceGainStatsResult)
def calculate_crit_chance_gain(data: CritChanceGainStatsInput):
    logger.info(f'/crit-chance-gain - Calculating crit chance gain with input: {data.model_dump()}')
    crit_chance_gain = hero_level_service.calculate_crit_chance_gain(data.player_level, data.enemy_level)

    result = {'crit_chance_gain': crit_chance_gain}

    logger.info(f'/crit-chance-gain - Crit chance gain for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/crit-power-gain', tags=[item_tag], response_model=CritPowerGainStatsResult)
def calculate_crit_power_gain(data: CritPowerGainStatsInput):
    logger.info(f'/crit-power - Calculating crit power gain with input: {data.model_dump()}')
    crit_power_gain = hero_level_service.calculate_crit_power_gain(data.player_level, data.enemy_level)

    result = {'crit_power_gain': crit_power_gain}

    logger.info(f'/crit-power - Crit power for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/item-armor', tags=[item_tag], response_model=ItemArmorStatsResult)
def calculate_item_armor(data: ItemArmorStatsInput):
    logger.info(f'/item-armor - Calculating item armor: {data.model_dump()}')
    armor = item_defense_service.calculate_item_armor(data.armor_factor, data.class_power, data.rarity_power, data.level_power)

    result = {'armor': armor}

    logger.info(f'/item-armor - Item armor for {data.model_dump()}: {result}')
    return result

@item_stats_router.post('/item-stats', tags=[item_tag], response_model=ItemStatsResult)
def calculate_item_stats(data: ItemStatsInput):
    logger.info(f'/item-stats - Calculating item stats: {data.model_dump()}')

    result = item_stats_service.calculate_item_stats(data)

    logger.info(f'/item-stats - Item stats for {data.model_dump()}: {result}')
    return result

@item_stats_router.get('/bless-legendary-chance', tags=[item_tag])
def bless_legendary_chance():
    key = 'legendary_bless_item_chance'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    logger.info(f'/bless-legendary-chance - Bless legendary items chance')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-rarity-amount', tags=[item_tag])
def item_rarity_amount():
    key = 'item_rarity_amount'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    logger.info(f'/item-rarity-amount - Item rarity amount')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-loot-chance', tags=[item_tag])
def item_lot_chance():
    key = 'item_loot_chance'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    logger.info(f'/item-loot-chance - Item lots chance')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-bonus-amount', tags=[item_tag])
def item_bonus_amount():
    key = 'item_bonus_amount'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    logger.info(f'/item-bonus-amount - Item bonus amount')
    return ALL_JSON_DATA[key]

@item_stats_router.get('/item-class-power', tags=[item_tag])
def item_class_power():
    key = 'item_class_power'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    logger.info(f'/item-class-power - Item class power')
    return ALL_JSON_DATA[key]

@legendary_bonus_router.post('/expiration', tags=[legendary_bonus_tag], response_model=LegendaryBonusResult)
def calculate_legendary_bonus_expiration(data: LegendaryBonusInput):
    logger.info(f'/legendary-bonus/expiration - Calculating legendary bonus with input: {data.model_dump()}')
    legendary_bonus_first_nerf = legendary_bonus_service.calculate_first_nerf_level(data.item_level)
    legendary_bonus_expiration = legendary_bonus_service.calculate_legendary_bonus_expiration(data.item_level)

    result = {
        'first_nerf_level': legendary_bonus_first_nerf,
        'expiration_level': legendary_bonus_expiration,
    }

    logger.info(f'/legendary-bonus/expiration - Legendary bonus expiration for {data.model_dump()}: {result}')
    return result

@legendary_bonus_router.get('/bonuses', tags=[legendary_bonus_tag])
def legendary_bonuses_names_and_chances():
    key = 'legendary_bonuses'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    logger.info(f'/legendary-bonus/bonuses - Legendary bonuses')
    return ALL_JSON_DATA[key]

@legendary_bonus_router.post('/very-crit', tags=[legendary_bonus_tag], response_model=VeryCritResult)
def calculate_very_crit(data: VeryCritInput):
    logger.info(f'/legendary-bonus/very-crit - Calculating very-crit with input: {data.model_dump()}')
    very_crit_chance = legendary_bonus_service.calculate_very_crit_chance(data.crit_chance)
    very_crit_power = legendary_bonus_service.calculate_very_crit_power(data.crit_power, data.crit_chance)

    result = {
            'very_crit_chance': very_crit_chance,
            'very_crit_power': very_crit_power
    }

    logger.info(f'/legendary-bonus/very-crit - Very crit stats for {data.model_dump()}: {result}')
    return result

@legendary_bonus_router.post('/holy-touch', tags=[legendary_bonus_tag], response_model=HolyTouchResult)
def calculate_holy_touch(data: HolyTouchInput):
    logger.info(f'/legendary-bonus/holy-touch - Calculating holy touch with input: {data.model_dump()}')
    healing_per_round = legendary_bonus_service.calculate_holy_touch_heal_value(data.hp)
    rounds = 3
    total_healing = healing_per_round * rounds

    result = {
        'healing_per_round': healing_per_round,
        'rounds': rounds,
        'total_healing': total_healing
    }

    logger.info(f'/legendary-bonus/holy-touch - Holy touch stats for {data.model_dump()}: {result}')
    return result

@legendary_bonus_router.post('/anguish', tags=[legendary_bonus_tag], response_model=AnguishResult)
def calculate_anguish(data: AnguishInput):
    logger.info(f'/legendary-bonus/anguish - Calculating anguish with input: {data.model_dump()}')
    anguish_damage = legendary_bonus_service.calculate_anguish_damage(data.level, data.strength, data.intellect, data.agility)

    result = { 'damage': anguish_damage }

    logger.info(f'/legendary-bonus/anguish - Anguish stats for {data.model_dump()}: {result} ')
    return result
