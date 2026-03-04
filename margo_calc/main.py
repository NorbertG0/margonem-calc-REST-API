from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from limiter import limiter
from api.calculator import router
from api.calculator import legendary_bonus_router

app = FastAPI()

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
async def ratelimit_handler(request: Request, exc):
    return JSONResponse(status_code=429, content={'message': 'Rate limit exceeded'})

app.include_router(router)
app.include_router(legendary_bonus_router)
