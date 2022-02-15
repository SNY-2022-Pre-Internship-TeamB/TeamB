import sys
import os
from typing import Optional
from fastapi import APIRouter, Body, status, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi import Query

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from database import *
from model import *

router = APIRouter()

@router.get("", responses = {200 : {"model" : PolicySchema},
                             404 : {"model" : ErrorResponseModel}})
async def get_policy(u_region : Optional[str] = Query(None, description = "사용자의 지역 [Optional]"),
                     u_age : Optional[int] = Query(None, description = "사용자의 나이 [Optional]"),
                     policy_type : Optional[str] = Query(None, description = "사용자가 선택한 정책 유형 [Optional]"),
                     p_name : Optional[str] = Query(None, description = "정책의 이름 [Optional]")):

    if u_region and u_age and policy_type:
        policies = await retrieve_policies_by_user(u_region, u_age, policy_type)
    elif p_name:
        policies = await retrieve_policies_by_name(p_name)
    else:
        policies = await retrieve_all_policies()

    if policies:
        return okResponse(200, policies)
    else:
        return errorResponse(404, "There are no policies")

@router.post("", responses = {202 : {"model" : AsyncResponseModel}})
async def post_policy(background_tasks : BackgroundTasks, policy : PolicySchema = Body(...)):
    policy = jsonable_encoder(policy)
    background_tasks.add_task(add_policy, policy)

    return asyncResponse(202, "GET", "http://localhost:8000/policies/{}/details".format(policy['policy_id']))

@router.delete("", status_code = status.HTTP_204_NO_CONTENT, response_description = "Successfully deleted")
async def delete_policy(background_tasks : BackgroundTasks):
    background_tasks.add_task(delete_all_policy)

@router.put("")
async def put_policy():
    pass

@router.patch("")
async def patch_policy():
    pass

@router.options("")
async def options_policy():
    pass

@router.head("")
async def head_policy():
    pass