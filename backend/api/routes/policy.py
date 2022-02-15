import sys
import os
from fastapi import APIRouter, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi import Query

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from database import retrieve_all_policies, add_policy
from model import PolicySchema, AsyncResponseModel, AsyncResponse

router = APIRouter()

@router.get("")
async def get_all_policy(response : Response):
    policies = await retrieve_all_policies()

    if policies:
        response.status_code = status.HTTP_200_OK
        return policies

@router.post("", responses = {202 : {"model" : AsyncResponseModel}})
async def post_policy(policy : PolicySchema):
    policy = jsonable_encoder(policy)
    add_policy(policy)

    return AsyncResponse(202, "GET", "http://localhost:8000/policies/{}/details".format(policy['policy_id']))