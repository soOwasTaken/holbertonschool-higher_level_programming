#!/usr/bin/python3
"""Script that prints the State object with the name"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine to connect to database
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)
