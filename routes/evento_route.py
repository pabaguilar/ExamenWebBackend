from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, List

# -----------------------------------------

from models.evento_schema import eventoSchema
import item_logic.evento as evento_logic

# -----------------------------------------

router = APIRouter()

@router.post("/")
async def post_(input: eventoSchema = Body(...)):
    try:
        print(input)
        result = await evento_logic.post(input.model_dump())
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")

@router.put("/{id}")
async def put_(id: str,input: eventoSchema = Body(...)):
    try:
        result = await evento_logic.put(id,input.model_dump())
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update")

@router.delete("/{id}")
async def delete_(id: str):
    try:
        deleted = await evento_logic.delete(id)
        return deleted
    except Exception as e:
        print(f"Failed to delete entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete")


@router.get("/{id}")
async def get_by_id(id: str):
    try:
        result = await evento_logic.get_by_id(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve")




@router.get("/")
async def get_all(
    email: Optional[str] = Query(None),
    lat: Optional[float] = Query(None),
    lon: Optional[float] = Query(None)
):
    try:
        filter = {}
        if email:
            filter["email"] = {"$regex": ".*{}.*".format(email), "$options": "i"}
        if lat is not None:
            filter["lat"] = {"$gte": lat - 0.2, "$lte": lat + 0.2}
        if lon is not None:
            filter["lon"] = {"$gte": lon - 0.2, "$lte": lon + 0.2}

        usuarios = await evento_logic.get(filter)
        return usuarios

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Retrieve failed")


