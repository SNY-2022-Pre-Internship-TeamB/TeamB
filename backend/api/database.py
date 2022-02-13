from motor.motor_asyncio import AsyncIOMotorClient

async def db_connection():
    MONGODB_URL = "mongodb://3.39.15.18:27017"
    client = AsyncIOMotorClient(MONGODB_URL)
    database = client.SNdb
    policy_collection = database.get_collection("resultAll")
    return policy_collection

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

async def retrieve_policies(u_region, u_age, policy_type) -> dict:
    policy_collection = await db_connection()
    policies = []
    condition = {
        "p_region" : u_region,
        "p_age_max" : {"$gte" : u_age},
        "policy_type" : policy_type
    }
    async for policy in policy_collection.find(condition):
        policies.append(policy_name_helper(policy))

    return policies

async def retrieve_all_policies() -> dict:
    policy_collection = await db_connection()
    policies = []
    async for policy in policy_collection.find():
        policies.append(policy_name_helper(policy))

    return policies

async def retrieve_details(policy_id) -> dict:
    policy_collection = await db_connection()
    details = []
    condition = {
        "policy_id" : policy_id
    }
    async for detail in policy_collection.find(condition):
        details.append(policy_detail_helper(detail))

    return details

async def retrieve_all_details() -> dict:
    policy_collection = await db_connection()
    details = []
    async for detail in policy_collection.find():
        details.append(policy_detail_helper(detail))
    return details