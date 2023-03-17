#!/usr/bin/python3
"""
lists all State objects from the database test_7
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    # create a session factory to create sessions
    Session = sessionmaker(bind=engine)

    # create a session to query the database
    session = Session()

    # query the database to get all State objects
    states = session.query(State).order_by(State.id)

    # display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()
