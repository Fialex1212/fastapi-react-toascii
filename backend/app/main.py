from fastapi import FastAPI
from api import ascii
from cors import add_cors

app = FastAPI()
add_cors(app)
app.include_router(ascii.router, prefix="/api", tags=["api"])
