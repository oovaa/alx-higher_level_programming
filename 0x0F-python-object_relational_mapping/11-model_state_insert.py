#!/usr/bin/python3

"""a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    # 1. Create an instance of the model class
    new_state = State(name='Louisiana')

    # 2. Add the instance to the session
    session.add(new_state)

    # 3. Commit the session to persist the changes
    session.commit()

    # Access the newly added object's properties
    print(new_state.id)
