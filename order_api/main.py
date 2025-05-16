from fastapi import FastAPI

from order_api.api import router as api_router

app = FastAPI(title='My API', description='My API', version='v1')

app.include_router(api_router, prefix='/api')
