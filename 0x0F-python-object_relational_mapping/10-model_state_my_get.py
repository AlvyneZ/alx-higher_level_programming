#!/usr/bin/python3
"""
This script searches a MySQL DB for a state
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Searching for the state from database
    """
    n = len(argv)
    if n != 5:
        print(
            "Usage: {} mysql_username ".format(argv[0]) +
            "mysql_password database_name state_name"
        )
    else:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        instance = session.query(State)\
                .filter(State.name == argv[4])\
                .first()
        if instance is None:
            print('Not found')
        else:
            print(instance.id)
