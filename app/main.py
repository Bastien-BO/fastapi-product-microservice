#!user/bin/dev/env python3
# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.core.settings import get_settings
from app.routers.startup import router as router_startup


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Products API",
    description="",
    version="Bêta",
    debug=get_settings().api_debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_startup)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5001, log_level="info")
