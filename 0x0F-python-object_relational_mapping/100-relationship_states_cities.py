#!/usr/bin/python3
"""
a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)
"""
import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create tables in the correct order
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')

    newState.cities.append(newCity)

    session.add(newState)
    session.commit()
    session.close()
