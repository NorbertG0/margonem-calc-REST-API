from fastapi import APIRouter, HTTPException
from core.config import VERSION, LEGENDARY_BONUS_TAG
from core.data_loader import ALL_JSON_DATA
from loguru import logger

from services import legendary_bonuses as legendary_bonus_service

from schemas.legendary_bonuses import *
from schemas.common import *

legendary_bonus_router = APIRouter(prefix=f'/api/{VERSION}/legendary-bonus')

@legendary_bonus_router.post('/expiration', tags=[LEGENDARY_BONUS_TAG], response_model=LegendaryBonusResult)
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

@legendary_bonus_router.get('/bonuses', tags=[LEGENDARY_BONUS_TAG])
def legendary_bonuses_names_and_chances():
    key = 'legendary_bonuses'
    if key not in ALL_JSON_DATA:
        raise HTTPException(status_code=404, detail=f'{key} not found in data folder')
    return ALL_JSON_DATA[key]

@legendary_bonus_router.post('/very-crit', tags=[LEGENDARY_BONUS_TAG], response_model=VeryCritResult)
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

@legendary_bonus_router.post('/holy-touch', tags=[LEGENDARY_BONUS_TAG], response_model=HolyTouchResult)
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

@legendary_bonus_router.post('/anguish', tags=[LEGENDARY_BONUS_TAG], response_model=AnguishResult)
def calculate_anguish(data: AnguishInput):
    logger.info(f'/legendary-bonus/anguish - Calculating anguish with input: {data.model_dump()}')
    anguish_damage = legendary_bonus_service.calculate_anguish_damage(data.level, data.strength, data.intellect, data.agility)

    result = { 'damage': anguish_damage }

    logger.info(f'/legendary-bonus/anguish - Anguish stats for {data.model_dump()}: {result} ')
    return result
