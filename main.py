from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import ai

app = FastAPI(title="IA API Quick Integration")

@asynccontextmanager
async def lifespan(app: FastAPI):
    pass
    yield
    pass

app.router.lifespan_context = lifespan

app.include_router(ai.router)

@app.get("/")
def read_root():
    return {"IA API Quick Integration": "0.1.0"}
