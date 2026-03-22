from loguru import logger
from fastapi import APIRouter
from core.config import VERSION, CONFIG_TAG

config_router = APIRouter(prefix=f'/api/{VERSION}/config')

@config_router.get('/health', tags=[CONFIG_TAG])
def health():
    return {'status': 'ok'}
