#!/usr/bin/python3

"""
a script that changes the name of a State object
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

    # 1 get the state
    new_state = session.query(State).filter(State.id == 2).first()

    # 2 update it
    new_state.name = "New Mexico"

    # 3. Commit the session to persist the changes
    session.commit()

    # Access the newly added object's properties
    print(new_state.id)

    session.close()
