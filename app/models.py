from datetime import datetime

from sqlalchemy import Column,Integer,String,Boolean,DateTime,func
from .database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    description = Column(String(250),nullable=True)
    is_complate = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
