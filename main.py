from fastapi import FastAPI

from adapters.driving import vector_search_controller

app = FastAPI()

app.include_router(vector_search_controller.router, prefix="/api/v1", tags=["vector_search"])
