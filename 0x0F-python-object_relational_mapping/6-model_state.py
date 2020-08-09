#!/usr/bin/python3
"""Start link class to table in database"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement='auto'
    )
    name = Column(
        String(128),
        nullable=False
    )
