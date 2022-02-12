import sys
import os
from fastapi import APIRouter
from fastapi import Query

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from database import retrieve_details

router = APIRouter()

@router.get("", response_description = "Get Policy Detail")
async def get_policy_detail(policy_number : str = Query(None, description = "정책 번호")):
    details = await retrieve_details(policy_number)
    if details:
        return details