import sys
import os
from fastapi import APIRouter, Body, status, BackgroundTasks, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Path

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from database import *
from model import *

router = APIRouter()

@router.get("", responses = {200 : {"model" : PolicySchema},
                             404 : {"model" : ErrorResponseModel}})
async def get_policy_detail(policy : str = Path(..., description = "정책 번호 또는 이름")):
    if policy.startswith("R"):
        details = await retrieve_details_by_id(policy)
    else:
        details = await retrieve_details_by_name(policy)

    if details:
        return okResponse(200, details)
    else:
        return errorResponse(404, "There are no policies")

@router.post("", responses = {202 : {"model" : AsyncResponseModel}})
async def post_policy(background_tasks : BackgroundTasks, policy : str = Path(..., description = "정책 번호 또는 이름"),
                      policy_post : PolicySchema = Body(...)):
    policy_post = jsonable_encoder(policy_post)
    background_tasks.add_task(add_policy, policy_post)

    return asyncResponse(202, "GET", "http://localhost:8000/policies/{}".format(policy))

@router.delete("", status_code = status.HTTP_204_NO_CONTENT, response_description = "Successfully deleted")
async def delete_policy(background_tasks : BackgroundTasks, policy : str = Path(..., description = "정책 번호 또는 이름")):
    if policy.startswith("R"):
        background_tasks.add_task(delete_policy_by_id, policy)
    else:
        background_tasks.add_task(delete_policy_by_name, policy)

    return JSONResponse(status_code = 204)

@router.options("")
async def options_policy(response : Response, policy : str = Path(..., description = "정책 번호 또는 이름")):
    response.headers["Allow"] = "GET, PUT, POST, DELETE, OPTIONS, HEAD, PATCH"

@router.head("", responses = {200 : {},
                              404 : {}})
async def head_policy(policy : str = Path(..., description = "정책 번호 또는 이름")):

    if policy.startswith("R"):
        details = await retrieve_details_by_id(policy)
    else:
        details = await retrieve_details_by_name(policy)

    if details:
        return JSONResponse(status_code = 200)
    else:
        return JSONResponse(status_code = 404)

@router.put("")
async def put_policy(background_tasks : BackgroundTasks, policy : str = Path(..., description = "정책 번호 또는 이름")):
    pass

@router.patch("")
async def patch_policy(policy : str = Path(..., description = "정책 번호 또는 이름")):
    pass