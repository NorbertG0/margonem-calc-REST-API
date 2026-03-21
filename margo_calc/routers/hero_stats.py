from fastapi import APIRouter
from core.config import VERSION, STATS_TAG
from loguru import logger

from services import strength as strength_service
from services import intellect as intellect_service
from services import dexterity as dexterity_service
from services import evade as evade_service
from services import block as block_service
from services import hero_level as hero_level_service

from schemas.basic_stats import *
from schemas.common import *
from schemas.item_stats import *

hero_stats_router = APIRouter(prefix=f'/api/{VERSION}/hero-stats')

@hero_stats_router.post('/base-stats', tags=[STATS_TAG], response_model=HeroLevelStatsResult)
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

@hero_stats_router.post('/exp-amount', tags=[STATS_TAG], response_model=HeroExpAmountResult)
def calculate_exp_amount(data: HeroExpAmountInput):
    logger.info(f'/exp-amount - Calculating exp amount with input: {data.model_dump()}')
    exp_amount = hero_level_service.calculate_exp_amount(data.level)

    result = {'exp_amount': exp_amount}

    logger.info(f'/exp-amount - Exp amount for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/experience', tags=[STATS_TAG], response_model=HeroExperienceResult)
def calculate_experience(data: HeroExperienceInput):
    logger.info(f'/experience - Calculating experience with input: {data.model_dump()}')
    experience = hero_level_service.calculate_experience(data.player_level, data.npc_level)

    result = {'experience': experience}

    logger.info(f'/experience - Experience for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/experience-penalty', tags=[STATS_TAG], response_model=ExperiencePenaltyResult)
def calculate_experience_penalty(data: ExperiencePenaltyInput):
    logger.info(f'/experience-penalty - Calculating experience penalty with input: {data.model_dump()}')
    experience_penalty = hero_level_service.calculate_experience_penalty(data.player_level, data.npc_level)

    result = {'experience_penalty': experience_penalty}

    logger.info(f'/experience-penalty - Experience penalty for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/highest-level', tags=[STATS_TAG], response_model=HighestLevelInGroupResult)
def calculate_highest_level_in_group(data: HighestLevelInGroupInput):
    logger.info(f'/highest-level - Calculating highest level in group with input: {data.model_dump()}')
    max_level = hero_level_service.calculate_highest_level_in_group(data.server_factor, data.level_ally_min)

    result = {'max_level': max_level}

    logger.info(f'/highest-level - Highest level in group {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/strength', tags=[STATS_TAG], response_model=StrengthStatsResult)
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

@hero_stats_router.post('/intellect', tags=[STATS_TAG], response_model=IntellectStatsResult)
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

@hero_stats_router.post('/dexterity', tags=[STATS_TAG], response_model=DexterityStatsResult)
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

@hero_stats_router.post('/evade', tags=[STATS_TAG], response_model=EvadeStatsResult)
def calculate_evade_percentage(data: EvadeStatsInput):
    logger.info(f'/evade - Calculating evade percentage with input: {data.model_dump()}')
    evade_percentage = evade_service.calculate_evade(data.evade, data.enemy_level)

    result = {'evade_percentage': evade_percentage}

    logger.info(f'/evade - Evade percentage for {data.model_dump()}: {result}')
    return result

@hero_stats_router.post('/block', tags=[STATS_TAG], response_model=BlockStatsResult)
def calculate_block_percentage(data: BlockStatsInput):
    logger.info(f'/block - Calculating block percentage with input: {data.model_dump()}')
    block_percentage = block_service.calculate_block(data.block, data.enemy_level)

    result = {'block_percentage': block_percentage}

    logger.info(f'/block - Block percentage for {data.model_dump()}: {result}')
    return result