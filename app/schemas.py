from datetime import datetime
from pydantic import BaseModel, Field


# Umumiy schema
class TodoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = Field(None, max_length=250)
    is_complate: bool = False


# Yangi todo yaratishda
class TodoCreate(TodoBase):
    pass


# Todo yangilaganda
class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=100)
    description: str | None = Field(None, max_length=250)
    is_complate: bool | None = None


# Foydalanuvchiga qaytariladigan schema
class TodoOut(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
