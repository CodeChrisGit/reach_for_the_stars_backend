import os
import uvicorn
from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Reach for the Stars API")

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Reach for the Stars API is running!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3001))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)