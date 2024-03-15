#!/usr/bin/python3
"""
Module city
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for instance in (session.query(State, City)
                     .filter(State.id == City.state_id)):
        print(instance.State.name + ": (" + str(instance.City.id) + ") " + instance.City.name)

    session.close()
