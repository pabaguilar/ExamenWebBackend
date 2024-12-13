from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import List
from datetime import datetime, timezone, timedelta


class logSchema(BaseModel):
    timestamp: datetime = Field(...)
    email: str = Field(min_length=1)
    token: str = Field(min_length=1)

    model_config = {
        "json_schema_extra": {
            "example": {
                "timestamp": "2014-12-31T10:30:00.000",
                "email": "pablo@uma.es",
                "token": "1111dqwu1892d10j",
            }
        }
    }