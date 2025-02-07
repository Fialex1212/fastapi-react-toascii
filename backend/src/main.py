from fastapi import FastAPI
from routers import router
from cors import add_cors

app = FastAPI()
add_cors(app)
app.include_router(router, prefix="/api", tags=["api"])