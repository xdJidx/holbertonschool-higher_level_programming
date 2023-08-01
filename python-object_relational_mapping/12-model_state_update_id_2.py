#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # Replace 'localhost' with your MySQL server hostname if needed
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State object with id = 2
    state_id_to_update = 2
    state_to_update = session.query(State) \
        .filter_by(id=state_id_to_update).first()

    # Check if the State object exists
    if state_to_update is None:
        print("State with id = {} not found".format(state_id_to_update))
    else:
        # Update the name of the State object
        new_name = "New Mexico"
        state_to_update.name = new_name
        session.commit()

    # Close the session
    session.close()
