#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
