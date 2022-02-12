from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from routes.policy_name import router as PolicyNameRouter
from routes.policy_details import router as PolicyDetailRouter

app = FastAPI()
app.include_router(PolicyNameRouter, tags = ["Policy Name"], prefix = "/policy")
app.include_router(PolicyDetailRouter, tags = ["Policy Detail"], prefix = "/detail")
Instrumentator().instrument(app).expose(app)