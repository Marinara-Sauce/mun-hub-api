import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from src.database import database as database
from src.endpoints import participant_endpoints, delegation_endpoints, committee_endpoints, speakerlist_endpoints

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

# build tables
database.Base.metadata.create_all(bind=database.engine)

# routers
app.include_router(committee_endpoints.router)
app.include_router(delegation_endpoints.router)
app.include_router(participant_endpoints.router)
app.include_router(speakerlist_endpoints.router)


@app.get("/ping", tags=['Basic'])
async def root():
    return {"message": "Success"}
