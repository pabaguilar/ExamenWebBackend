from database import MONGOCRUD
# from models.primer_schema import Invitados
from bson import ObjectId  # Importar ObjectId desde bson
import item_logic.log as segundologic
from typing import Optional, List
from datetime import datetime, timedelta

class EventoCrud(MONGOCRUD):

    def __init__(self):
        super().__init__('Evento')

    async def delete_secundario_by(self,email: str):
        deleted = False
        item = await self.collection.find_one({'email': email})
        if item:
            await self.collection.delete_one({"email": email})
            deleted = True
        return deleted

    async def update_secundario_by(self,email: str, data: dict):
        if not data:
            return False
        item = await self.collection.find_one({'email': email})
        # item = await self.collection.find_one({"email": ObjectId(email)})

        if item:
            updatedItem = await self.collection.update_one(
                {"email": email}, {"$set": data}
            )
            return bool(updatedItem)

        return False
