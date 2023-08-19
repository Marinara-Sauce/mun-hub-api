from fastapi import FastAPI

from src.database import database as database
from src.endpoints import participant_endpoints, delegation_endpoints, committee_endpoints

app = FastAPI()

# build tables
database.Base.metadata.create_all(bind=database.engine)

# routers
app.include_router(committee_endpoints.router)
app.include_router(delegation_endpoints.router)
app.include_router(participant_endpoints.router)


@app.get("/ping", tags=['Basic'])
async def root():
    return {"message": "Success"}
