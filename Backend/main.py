from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.jwt_auth.router import router as jwt_router
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jwt_router)

@app.get("/healthcheck", tags=["Healthcheck"], summary="Проверка работоспособности сервера")
def healthcheck():
    return {"message": "server is ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)