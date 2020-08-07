#!/usr/bin/python3
""" State ORM object"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ ORM class for state """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
