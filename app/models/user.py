from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    # task_id = Column(Integer, ForeignKey('tasks.id'))

    tasks = relationship('Task', back_populates='user')
# tasks - объект связи с таблицей Task, где back_populates='user'.
# ategory = relationship('Category', back_populates='products')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
