from fastapi import FastAPI
from pydantic import BaseModel

from app.server.routes.service_routes import router as Router
from typing import List


app = FastAPI()
app.include_router(Router, tags=["Graph Scrutinizer"], prefix="/scrutinizer")

@app.get("/", tags=["Root"])
async def read_root():
    return {"status": "OK"}


