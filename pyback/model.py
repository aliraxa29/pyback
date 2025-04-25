# framework/model.py

import datetime
from pydantic import BaseModel

class DocType(BaseModel):
    name: str
    creation: datetime.datetime
    modified: datetime.datetime
    modified_by: str
    owner: str

    class Config:
        orm_mode = True