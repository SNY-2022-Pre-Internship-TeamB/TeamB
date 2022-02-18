from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from routes.policy import router as PolicyRouter
from routes.policy_details import router as PolicyDetailByIdRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(PolicyRouter, tags = ["정책명 조회"], prefix = "/policies")
app.include_router(PolicyDetailByIdRouter, tags = ["정책 번호 또는 이름으로 세부내용 조회"], prefix = "/policies/{policy}")

Instrumentator().instrument(app).expose(app)