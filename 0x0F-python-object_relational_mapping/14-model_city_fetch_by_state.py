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
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Use all() to retrieve all instances that match the condition
    instances_to_delete = session.query(
        State.name, City.id, City.name).filter(
            State.id == City.state_id)

    # Delete the instances
    for instance in instances_to_delete:
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
