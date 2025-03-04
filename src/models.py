from pydantic import BaseModel
from sqlalchemy import JSON, Column
from sqlmodel.main import SQLModel, Field

class Nyx(BaseModel):
    id_tipo: int
    fields: dict = Field(default_factory=dict)
    
    
class NyxSQL(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_tipo: int
    fields: dict = Field(sa_column=Column(JSON), default_factory=dict)