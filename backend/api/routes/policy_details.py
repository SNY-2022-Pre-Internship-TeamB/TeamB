import sys
import os
from fastapi import APIRouter, Query, Path

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