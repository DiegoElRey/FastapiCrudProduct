from app.routes.user import router as user_router
from app.routes.product import router as product_router
from fastapi import FastAPI, Request, Response



app = FastAPI()




@app.middleware("http")
async def custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Custom header value"
    return response


@app.get("/")
async def root():
    return {"message": "La aplicacion esta funcionando!"}


# app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/products", tags=["products"])
