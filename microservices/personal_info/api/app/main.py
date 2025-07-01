from fastapi import FastAPI

app = FastAPI(
    title="Job Hunting Ai",
    version="1.0.0",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint to verify if the service is running.
    """
    return {"status": "ok"}


