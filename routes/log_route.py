from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, List

# -----------------------------------------

from models.log_schema import logSchema
import item_logic.log as log_logic

# -----------------------------------------

router = APIRouter()

@router.post("/")
async def post_(input: logSchema = Body(...)):
    try:
        result = await log_logic.post(input.model_dump())
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")

@router.put("/{id}")
async def put_(id: str,input: logSchema = Body(...)):
    try:
        result = await log_logic.put(id,input.model_dump())
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update")


@router.delete("/{id}")
async def delete_(id: str):
    try:
        deleted = await log_logic.delete(id)
        return deleted
    except Exception as e:
        print(f"Failed to delete entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete")


# @router.get("/{id}")
# async def get_by_id(id: str):
#     try:
#         result = await log_logic.get_by_id(id)
#         return result
#     except Exception as e:
#         print(f"Failed to retrieve entry: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to retrieve")


# GET ALL
@router.get("/")
async def get_logs(filter_user: Optional[str] = Query(None)):
    filter = {}

    if filter_user:
        filter["email"] = filter_user

    result = await log_logic.get(filter)

    return result
