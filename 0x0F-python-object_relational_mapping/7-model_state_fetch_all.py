#!/usr/bin/python3

"""a script that lists all State
objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection_string = "mysql+mysqlconnector://{}:{}@localhost:3306/{}".
    format(argv[1], argv[2], argv[3])

    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    table_data = session.query(State).order_by(State.id)

    for state in table_data:
        print(state.id, state.name, sep=": ")

    session.close()
