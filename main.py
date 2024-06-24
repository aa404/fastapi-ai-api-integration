from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import ai
import logging

app = FastAPI(title="IA API Quick Integration")

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
