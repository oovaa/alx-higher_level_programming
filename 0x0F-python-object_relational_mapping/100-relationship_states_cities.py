#!/usr/bin/python3
"""
a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":

    # Connect to the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the database tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Define state and city names
    state_name = "California"
    city_name = "San Francisco"

    # Create instances of State and City
    new_state = State(name=state_name)
    new_city = City(name=city_name)

    # Establish the relationship by appending the city to the state's cities list
    new_state.cities.append(new_city)

    # Add the state to the session and commit changes
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
