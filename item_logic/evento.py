from item_logic.crud_inheritance.evento_crud import EventoCrud
from fastapi.encoders import jsonable_encoder

crud = EventoCrud()

async def post(input):
    result = await crud.create_item(input)
    return result

async def put(id,data):
    result = await crud.update_id(id,data)
    return result

async def get(filter):
    results = []
    if len(filter)>0:
        results = await crud.get_by_filter(filter)
    else:
        results = await crud.get_collection()
    return results

async def get_by_id(id):
    result = await crud.get_id(id)
    return result

async def delete(id):
    deleted = await crud.delete_id(id)
    return deleted




async def delete_by(idsecun):
    deleted = await crud.delete_secundario_by(idsecun)
    return deleted


async def put_by(idsecun,data):
    result = await crud.update_secundario_by(idsecun,data)
    return result

async def get_secundario(email):
    filter = {}
    filter["email"] = {"$regex": ".*{}.*".format(email), "$options": "i"}
    user = await crud.encuentra_uno(filter)
    return user

