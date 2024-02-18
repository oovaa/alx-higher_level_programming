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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = "California"
    city_name = "San Francisco"

    new_state = State()
    new_city = City()

    new_city.name = city_name
    new_state.name = state_name

    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()
