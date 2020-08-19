#!/usr/bin/python3
"""lists all State objects, and corresponding City objects"""

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

    state = session.query(State).order_by(State.id)
    for st in state:
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("    {}: {}".format(ct.id, ct.name))

    session.close()
