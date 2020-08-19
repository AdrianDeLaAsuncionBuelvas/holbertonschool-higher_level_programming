#!/usr/bin/python3
"""Relation City with State Module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """City class Module"""

    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement='auto',
                unique=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=True)
