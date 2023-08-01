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

    # Retrieve all State objects with a name containing the letter 'a'
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
                session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
