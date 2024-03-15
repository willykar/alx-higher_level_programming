#!/usr/bin/python3
"""model_state"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class city(Base):
    """inherits from Base
    Attributes:
    id (int)
    name (string)
    state_id (string)
    """
    __tablename__ = cities
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
