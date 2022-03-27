from fastapi import FastAPI
from routes.client import client

app = FastAPI()
app.include_router(client)