#/usr/bin/python3
# Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    add_state = State(name= "Louisiana")
    session.add()
    print(session.query(State).filter_by(name="Louisiana").first().id)

    session.commit()
    session.close()
