from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from api import calculator
from limiter import limiter
from api.calculator import router, legendary_bonus_router, config_router, hero_stats_router, item_stats_router
from loguru import logger
import time
import uuid

logger.remove()
logger.add('app.log', rotation='10 MB', retention='7 days', level='INFO', format='{time} | {level} | {message}', enqueue=True)
app = FastAPI()

version = 'v1'
@app.get('/')
def root_path():
    return {
        'name': 'margo-calc-api',
        'version': version,
        'status': 'ok',
        'docs': '/docs',
        'redoc': '/redoc',
    }

@app.middleware('http')
async def log_requests(request: Request, call_next):
    start_time = time.time()
    method = request.method
    url = request.url.path
    response = await call_next(request)
    process_time = round((time.time() - start_time) * 1000, 2)
    status_code = response.status_code
    request_id = str(uuid.uuid4())

    logger.info(f'{request_id} | {method} {url} | {status_code} | {process_time}ms')

    return response

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
async def ratelimit_handler(request: Request, exc):
    return JSONResponse(status_code=429, content={'message': 'Rate limit exceeded'})

app.include_router(router)
app.include_router(hero_stats_router)
app.include_router(item_stats_router)
app.include_router(legendary_bonus_router)
app.include_router(config_router)
