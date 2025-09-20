from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Encurtador de URLs - API",
    description="Encurtador de URLs em Python e FastAPI",
    version="1.0.0"
)

app.include_router(endpoints.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "API rodando, chefe. Manda brasa!"}