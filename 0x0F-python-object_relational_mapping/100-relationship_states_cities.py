#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

from relationship_state import Base, State
from relationship_city import City
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

    ct = State(name='California')
    st = City(name='San Francisco')
    ct.cities.append(st)
    session.add(ct)
    session.commit()

    session.close()
