#!/usr/bin/python3
"""
script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
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

    # Search for the State object with the given name
    state_name_to_search = sys.argv[4]
    state = session.query(State) \
        .filter(State.name == state_name_to_search).first()

    # Display the results
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
