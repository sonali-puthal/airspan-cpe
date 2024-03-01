import logging
import uvicorn
from fastapi import FastAPI
from app.api.endpoints import airspan
from app.core.config import initialize_logging

app = FastAPI()


app.include_router(
    airspan.router,
    prefix="/api/v1/airspan",
    tags=["airspan-cpe"],
)


@app.get("/")
async def root():
    return {"message": "INTAF CPE Automation API v1"}


if __name__ == "__main__":
    initialize_logging(
        filename="logs/app.log",  # relative to the cwd
        log_level_file=logging.DEBUG,
        log_level_console=logging.DEBUG,
    )
    uvicorn.run("main:app", port=5000, log_level=logging.DEBUG)
