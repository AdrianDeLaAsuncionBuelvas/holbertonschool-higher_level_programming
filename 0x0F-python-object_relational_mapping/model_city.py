#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py that \
contains the class definition of a City."""

from model_state import Base
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
