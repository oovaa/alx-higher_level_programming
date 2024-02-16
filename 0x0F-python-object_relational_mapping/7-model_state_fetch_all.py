#!/usr/bin/python3

"""a script that lists all State
objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    connection_string = "mysql+mysqlconnector://{}:{}@localhost:3306/{}".
    format(argv[1], argv[2], argv[3])

    engine = create_engine(connection_string)

    Session = sessionmaker(bind=engine)

    session = Session()

    table_data = session.query(State).all()

    for state in table_data:
        print(f"ID: {state.id}, Name: {state.name}")

    session.close()
