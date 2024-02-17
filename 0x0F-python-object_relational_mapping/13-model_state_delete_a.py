#!/usr/bin/python3

"""
Write a script that deletes all State objects
with a name containing the letter a
from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_instance = session.query(State).filter(State.name.like("%a%"))

    if new_instance:
        new_instance.delete()
        session.commit()
