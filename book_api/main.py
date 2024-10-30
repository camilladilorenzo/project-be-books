import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI
from book_api.api.endpoints import router as api_router
from book_api.core.config import Settings
from book_api.core.openapi import custom_openapi
import uvicorn

settings = Settings()

# Initialization
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(api_router)

# Customization of the OpenAPI schema
app.openapi = lambda: custom_openapi(app)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
