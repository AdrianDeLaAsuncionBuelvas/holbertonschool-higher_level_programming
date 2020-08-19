#!/usr/bin/python3
"""Relation City with State Module"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


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
