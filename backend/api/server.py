from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from routes.policy_name import router as PolicyNameRouter
from routes.policy_details import router as PolicyDetailRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(PolicyNameRouter, tags = ["정책명 조회"], prefix = "/policies")
app.include_router(PolicyDetailRouter, tags = ["정책 세부내용 조회"], prefix = "/details")

Instrumentator().instrument(app).expose(app)