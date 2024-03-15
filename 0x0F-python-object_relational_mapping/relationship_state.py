#!/usr/bin/python3
""" a python file that contains the class definition of a State
and an instance Base = declarative_base()"""


from sqlalchemy import Integer, String, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """inherits from Base
    Attributes:
    id (int)
    name (string)
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
