#!/usr/bin/python3

"""a script that prints the count of State objects
from the database hbtn_0e_6_usa with a specific name
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

    state_name = sys.argv[4]

    count_states_with_name = session.query(State).filter(
        State.name.like(f"{state_name}"))

    print(count_states_with_nameid)

    session.close()
