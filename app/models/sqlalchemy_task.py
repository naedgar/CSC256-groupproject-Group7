# app/models/sqlalchemy_task.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

"""
This model is designed for use with SQLite as the database, using SQLAlchemy as the ORM (Object Relational Mapper).
SQLAlchemy handles the translation between Python objects and database tables, and DeclarativeBase (SQLAlchemy 2.0+) ensures type checking works with tools like mypy.
You can use this model with any SQLAlchemy-supported database, but SQLite is used for this project development and testing because it requires no setup.
"""
# SQLAlchemy 2.0+ uses DeclarativeBase for models, which is fully compatible with mypy and avoids type errors.

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)
    created_at = Column(String, nullable=True)  # Store as ISO 8601 string from TimeService

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed}, created_at='{self.created_at}')>"