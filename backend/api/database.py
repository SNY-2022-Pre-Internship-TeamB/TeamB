from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

def db_connection():
    MONGODB_URL = "mongodb://3.39.15.18:27017"
    client = AsyncIOMotorClient(MONGODB_URL)
    database = client.SNdb
    policy_collection = database.get_collection("resultAll")
    return policy_collection

def policy_helper(policy) -> dict:
    return {
        "p_name" : policy["p_name"],
        "policy_id" : policy["policy_id"],
        "introduction": policy["introduction"],
        "policy_type": policy["policy_type"],
        "support": policy["support"],
        "operating_period" : policy["operating_period"],
        "application_period" : policy["application_period"],
        "scale" : policy["scale"],
        "p_region" : policy["p_region"],
        "p_age_max" : policy["p_age_max"],
        "p_age" : policy["p_age"],
        "p_region_income": policy["p_region_income"],
        "p_education" : policy["p_education"],
        "p_major1" : policy["p_major1"],
        "p_employment" : policy["p_employment"],
        "p_major2" : policy["p_major2"],
        "detail": policy["detail"],
        "restriction": policy["restriction"],
        "procedure": policy["procedure"],
        "announcement": policy["announcement"],
        "m_site": policy["m_site"],
        "document": policy["document"],
        "etc": policy["etc"],
        "a_name" : policy["a_name"],
        "m_name": policy["m_name"],
        "a_site1" : policy["a_site1"],
        "a_site2" : policy["a_site2"]
    }

def policy_name_helper(policy) -> dict:
    return {
        "policy_id" : policy["policy_id"],
        "p_name" : policy["p_name"]
    }

def policy_detail_helper(detail) -> dict:
    return {
        "introduction" : detail["introduction"],
        "policy_type" : detail["policy_type"],
        "support" : detail["support"],
        "p_region_income" : detail["p_region_income"],
        "detail": detail["detail"],
        "restriction": detail["restriction"],
        "procedure": detail["procedure"],
        "announcement": detail["announcement"],
        "m_site": detail["m_site"],
        "document": detail["document"],
        "etc": detail["etc"],
        "a_name": detail["a_name"]
    }

async def retrieve_all_policies() -> dict:
    policy_collection = db_connection()
    policies = []
    async for policy in policy_collection.find():
        policies.append(policy_helper(policy))

    return policies

def add_policy(policy_data : dict) -> dict:
    policy_collection = db_connection()
    policy_collection.insert_one(policy_data)

async def retrieve_policies(u_region, u_age, policy_type) -> dict:
    policy_collection = db_connection()
    policies = []
    condition = {
        "$or" : [{"p_region" : u_region}, {"p_region" : "중앙부처"}],
        "p_age_max" : {"$gte" : u_age},
        "policy_type" : policy_type
    }
    async for policy in policy_collection.find(condition):
        policies.append(policy_name_helper(policy))

    return policies

async def retrieve_details(policy_id) -> dict:
    policy_collection = db_connection()
    details = []
    condition = {
        "policy_id" : policy_id
    }
    async for detail in policy_collection.find(condition):
        details.append(policy_detail_helper(detail))

    return details

async def retrieve_all_details() -> dict:
    policy_collection = db_connection()
    details = []
    async for detail in policy_collection.find():
        details.append(policy_detail_helper(detail))

    return details