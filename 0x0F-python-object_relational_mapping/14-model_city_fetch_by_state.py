#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).filter(
            City.state_id == State.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
