from fastapi import APIRouter, Request

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
from services.legendary_bonuses import NAMES_AND_CHANCES

from additional_functions import calculate_range

RANGE_NEG2_5 = range(-2, 6)
RANGE_0_5 = range(0, 6)

version = 'v1'
router = APIRouter(prefix=f'/api/{version}')
legendary_bonus_router = APIRouter(prefix=f'/api/{version}/legendary-bonus')

stats_tag = 'Hero stats'
item_tag = 'Items stats'
legendary_bonus_tag = 'Legendary bonuses'

@router.post('/base-stats', tags=[stats_tag], response_model=HeroLevelStatsResult)
def calculate_base_hp(data: HeroLevelStatsInput):
    base_hp = hero_level_service.calculate_base_hp(data.level)
    base_crit_value =  hero_level_service.calculate_base_crit_value(data.level)

    return {
        'base_hp': base_hp,
        'base_crit_value': base_crit_value
    }

@router.post('/strength', tags=[stats_tag], response_model=StrengthStatsResult)
def calculate_strength_stats(data: StrengthStatsInput):
    base_hp = strength_service.calculate_base_hp(data.strength)
    armor_hp = strength_service.calculate_armor_hp(data.strength, data.armor_level)
    crit_gain = strength_service.calculate_crit_value(data.strength, data.level)

    total_hp_gain = base_hp + armor_hp

    return {
        'base_hp_gain': base_hp,
        'armor_hp_gain': armor_hp,
        'total_hp_gain': total_hp_gain,
        'crit_value_gain': crit_gain
    }

@router.post('/intellect', tags=[stats_tag], response_model=IntellectStatsResult)
def calculate_intellect_stats(data: IntellectStatsInput):
    absorb_limit = intellect_service.calculate_absorb_limit(data.intellect)
    crit_gain = intellect_service.calculate_crit_value(data.intellect, data.level)

    return {
        'absorb_limit': absorb_limit,
        'crit_value_gain': crit_gain
    }

@router.post('/dexterity', tags=[stats_tag], response_model=DexterityStatsResult)
def calculate_dexterity_stats(data: DexterityStatsInput):
    attack_speed = dexterity_service.calculate_attack_speed(data.dexterity)
    evade_gain = dexterity_service.calculate_evade_gain(data.dexterity)

    return {
        'attack_speed': attack_speed,
        'evade_gain': evade_gain,
    }

@router.post('/evade', tags=[stats_tag], response_model=EvadeStatsResult)
def calculate_evade_percentage(data: EvadeStatsInput):
    evade_percentage = evade_service.calculate_evade(data.evade, data.enemy_level)

    return {'evade_percentage': evade_percentage}

@router.post('/block', tags=[stats_tag], response_model=BlockStatsResult)
def calculate_block_percentage(data: BlockStatsInput):
    block_percentage = block_service.calculate_block(data.block, data.enemy_level)

    return {'block_percentage': block_percentage}

@router.post('/item-power', tags=[item_tag], response_model=ItemPowerStatsResult)
def calculate_item_power(data: ItemPowerStatsInput):
    item_level_power = item_power_service.calculate_item_level_power(data.level)
    item_rarity_power = item_power_service.calculate_item_rarity_power(data.level, data.rarity_factor)

    return {
        'item_level_power': item_level_power,
        'item_rarity_power': item_rarity_power
    }

@router.post('/weapon-damage', tags=[item_tag], response_model=WeaponDamageStatsResult)
def calculate_weapon_damage(data: WeaponDamageStatsInput):
    item_damage = item_power_service.calculate_weapon_damage(data.weapon_factor, data.item_rarity_power, data.item_level_power)
    item_damage_top = item_damage  + item_damage * data.item_damage_spread
    item_damage_bottom = item_damage - item_damage * data.item_damage_spread

    return {
        'item_damage': item_damage,
        'item_damage_top': item_damage_top,
        'item_damage_bottom': item_damage_bottom
    }

@router.post('/weapon-slow', tags=[item_tag], response_model=WeaponSlowStatsResult)
def calculate_weapon_slow(data: WeaponSlowStatsInput):
    item_slow = item_power_service.calculate_weapon_slow(data.slow_factor, data.item_level)

    return {'item_slow': item_slow}

@router.post('/physical-damage-reduction', tags=[item_tag], response_model=ArmorPhysicalDamageReductionStatsResult)
def calculate_physical_damage_reduction(data: ArmorPhysicalDamageReductionStatsInput):
    damage_out = damage_types_service.calculate_physical_damage_reduction(data.damage_in, data.armor)

    return {'damage_out': damage_out}

@router.post('/range-damage-reduction', tags=[item_tag], response_model=ArmorRangeDamageReductionStatsResult)
def calculate_range_damage_reduction(data: ArmorRangeDamageReductionStatsInput):
    damage_out = damage_types_service.calculate_range_damage_reduction(data.damage_in, data.armor)

    return {'damage_out': damage_out}

@router.post('/secondary-damage-reduction', tags=[item_tag], response_model=ArmorSecondaryDamageReductionStatsResult)
def calculate_second_damage_reduction(data: ArmorSecondaryDamageReductionStatsInput):
    damage_out = damage_types_service.calculate_secondary_damage_reduction(data.damage_in, data.armor)

    return {'damage_out': damage_out}

@router.post('/fire-damage-reduction', tags=[item_tag], response_model=ArmorFireDamageReductionStatsResult)
def calculate_fire_damage_reduction(data: ArmorFireDamageReductionStatsInput):
    damage_out = damage_types_service.calculate_fire_damage_reduction(data.damage_in, data.armor)

    return {'damage_out': damage_out}

@router.post('/frost-damage-redution', tags=[item_tag], response_model=ArmorFrostDamageReductionStatsResult)
def calculate_frost_damage_reduction(data: ArmorFrostDamageReductionStatsInput):
    damage_out = damage_types_service.calculate_frost_damage_reduction(data.damage_in, data.armor)

    return {'damage_out': damage_out}

@router.post('/light-damage-reduction', tags=[item_tag], response_model=ArmorLightDamageReductionStatsResult)
def calculate_light_damage_reduction(data: ArmorLightDamageReductionStatsInput):
    damage_out = damage_types_service.calculate_light_damage_reduction(data.damage_in, data.armor)

    return {'damage_out': damage_out}

@router.post('/crit-chance-gain', tags=[item_tag], response_model=CritChanceGainStatsResult)
def calculate_crit_chance_gain(data: CritChanceGainStatsInput):
    crit_chance_gain = hero_level_service.calculate_crit_chance_gain(data.player_level, data.enemy_level)

    return {'crit_chance_gain': crit_chance_gain}

@router.post('/crit-power-gain', tags=[item_tag], response_model=CritPowerGainStatsResult)
def calculate_crit_power_gain(data: CritPowerGainStatsInput):
    crit_power_gain = hero_level_service.calculate_crit_power_gain(data.player_level, data.enemy_level)

    return {'crit_power_gain': crit_power_gain}

@router.post('/item-armor', tags=[item_tag], response_model=ItemArmorStatsResult)
def calculate_item_armor(data: ItemArmorStatsInput):
    armor = item_defense_service.calculate_item_armor(data.armor_factor, data.class_power, data.rarity_power, data.level_power)

    return {'armor': armor}

@router.post('/item-stats', tags=[item_tag], response_model=ItemStatsResult)
def calculate_item_stats(data: ItemStatsInput):

    all_stats = calculate_range(range(0, 7), lambda a: item_stats_service.calculate_all_stats(data.level, a))
    strength = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_strength(data.level, a))
    dexterity = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_dexterity(data.level, a))
    intellect = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_intellect(data.level, a))
    attack_speed = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_attack_speed(data.level, a))

    level_power = data.level_power or 1
    class_power = data.class_power or 1

    health_points = calculate_range(range(-2, 7), lambda a: item_stats_service.calculate_health_points(data.level, a, level_power, class_power))
    heal = calculate_range(range(0, 4), lambda a: item_stats_service.calculate_heal(data.level, a, level_power, class_power))
    armor = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_armor(a, level_power, class_power))
    poison_resistance = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_poison_res(a))
    evade = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_evade(a, data.level))
    block = calculate_range(range(-1, 6), lambda a: item_stats_service.calculate_block(a, data.level))
    weapon_armor_destruction = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_weapon_armor_destruction(a, level_power))
    armor_destruction = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_armor_destruction(a, level_power))
    resistance_destruction = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_resist_destruction(a))
    absorption = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_absorption(a, level_power, class_power))
    magic_absorption = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_magic_absorption(a, level_power, class_power))
    mana = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_mana(a, data.level))
    energy = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_energy(a, data.level))
    attack_speed_reduction = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_attack_speed_reduction(a, data.level))
    crit = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_crit(a))
    physical_crit_power = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_phisycal_crit_power(a))
    magic_crit_power = calculate_range(RANGE_NEG2_5, lambda a: item_stats_service.calculate_magic_crit_power(a))
    crit_chance_reduction = calculate_range(range(0, 4), lambda a: item_stats_service.calculate_crit_chance_reduction(a))
    energy_reduction_chance = calculate_range(range(0, 4), lambda a: item_stats_service.calculate_energy_reduction_chance(a))
    energy_reduction_value = item_stats_service.calculate_energy_reduction_value(data.level)
    mana_reduction_chance = calculate_range(range(0, 4), lambda a: item_stats_service.calculate_mana_reduction_chance(a))
    mana_reduction_value = item_stats_service.calculate_mana_reduction_value(data.level)
    evade_reduction = calculate_range(RANGE_0_5, lambda a: item_stats_service.calculate_evade_reduction(a, data.level))
    fire_resists = calculate_range(range(-3, 11), lambda a: item_stats_service.calculate_fire_resists(a))
    frost_resists = calculate_range(range(-3, 11), lambda a: item_stats_service.calculate_frost_resists(a))
    light_resists = calculate_range(range(-3, 11), lambda a: item_stats_service.calculate_light_resists(a))

    return {
        'all_stats': all_stats,
        'strength': strength,
        'dexterity': dexterity,
        'intellect': intellect,
        'attack_speed': attack_speed,
        'health_points': health_points,
        'heal': heal,
        'armor': armor,
        'poison_resistance': poison_resistance,
        'block': block,
        'evade': evade,
        'weapon_armor_destruction': weapon_armor_destruction,
        'armor_destruction': armor_destruction,
        'resistance_destruction': resistance_destruction,
        'absorption': absorption,
        'magic_absorption': magic_absorption,
        'mana': mana,
        'energy': energy,
        'attack_speed_reduction': attack_speed_reduction,
        'crit': crit,
        'physical_crit_power': physical_crit_power,
        'magic_crit_power': magic_crit_power,
        'crit_chance_reduction': crit_chance_reduction,
        'energy_reduction_chance': energy_reduction_chance,
        'energy_reduction_value': energy_reduction_value,
        'mana_reduction_chance': mana_reduction_chance,
        'mana_reduction_value': mana_reduction_value,
        'evade_reduction': evade_reduction,
        'fire_resists': fire_resists,
        'frost_resists': frost_resists,
        'light_resists': light_resists,
    }

@router.post('/legendary-bonus/expiration', tags=[legendary_bonus_tag], response_model=LegendaryBonusResult)
def calculate_legendary_bonus_expiration(data: LegendaryBonusInput):
    legendary_bonus_first_nerf = legendary_bonus_service.calculate_first_nerf_level(data.item_level)
    legendary_bonus_expiration = legendary_bonus_service.calculate_legendary_bonus_expiration(data.item_level)

    return {
        'first_nerf_level': legendary_bonus_first_nerf,
        'expiration_level': legendary_bonus_expiration,
    }

@legendary_bonus_router.get('/bonuses', tags=[legendary_bonus_tag])
def legendary_bonuses_names_and_chances():
    return NAMES_AND_CHANCES

@legendary_bonus_router.post('/very-crit', tags=[legendary_bonus_tag], response_model=VeryCritResult)
def calculate_very_crit(data: VeryCritInput):
    very_crit_chance = legendary_bonus_service.calculate_very_crit_chance(data.crit_chance)
    very_crit_power = legendary_bonus_service.calculate_very_crit_power(data.crit_power, data.crit_chance)

    return {
            'very_crit_chance': very_crit_chance,
            'very_crit_power': very_crit_power
    }

@legendary_bonus_router.post('/holy-touch', tags=[legendary_bonus_tag], response_model=HolyTouchResult)
def calculate_holy_touch(data: HolyTouchInput):
    healing_per_round = legendary_bonus_service.calculate_holy_touch_heal_value(data.hp)
    rounds = 3
    total_healing = healing_per_round * rounds

    return {
        'healing_per_round': healing_per_round,
        'rounds': rounds,
        'total_healing': total_healing
    }

@legendary_bonus_router.post('/anguish', tags=[legendary_bonus_tag], response_model=AnguishResult)
def calculate_anguish(data: AnguishInput):
    anguish_damage = legendary_bonus_service.calculate_anguish_damage(data.level, data.strength, data.intellect, data.agility)

    return { 'damage': anguish_damage }
