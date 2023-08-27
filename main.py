import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# add mock data if dev
if os.getenv("ENVIRONMENT") != "production":
    with open("src/database/scripts/populate-mock-data.sql", "r") as sql_file:
        sql_script = sql_file.readlines()

    with database.engine.connect() as connection:
        for line in sql_script:
            connection.execute(text(line))
            
        connection.commit()
        connection.close()

# routers
app.include_router(committee_endpoints.router)
app.include_router(delegation_endpoints.router)
app.include_router(participant_endpoints.router)
app.include_router(speakerlist_endpoints.router)


@app.get("/ping", tags=['Basic'])
async def root():
    return {"message": "Success"}
